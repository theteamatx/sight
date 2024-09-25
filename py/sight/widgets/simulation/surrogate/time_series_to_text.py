
from dataclasses import dataclass
import numpy as np
import pandas as pd
from typing import List, Sequence


@dataclass
class Dataset:
  train: pd.DataFrame
  validate: pd.DataFrame
  max_input_len: int
  max_pred_len: int

def generate_prediction(row: np.ndarray, columns: Sequence[str]) -> str:
  """Returns the representation of row to use as the string the transformer will predict.
  
  Arguments:
    row: The data row, containing data for all the columns.
    columns: The names of the columns, one for each row element. Their names include the 
      prefix 'autoreg:', 'boundary:' or 'initial:' to indicate their role in the simulation.
  """
  data = []
  for i, c in enumerate(columns):
    if c.startswith('autoreg:'):
      data.append(str(row[i]))
  return ' '.join(data)

def generate_input(rows: Sequence[np.ndarray], next_row: np.ndarray, columns: Sequence[str]) -> str:
  """Returns the representation of rows to use as the string the transformer will take as input.
  
  Arguments:
    rows: The data rows, containing data for all columns.
    columns: The names of the columns, one for each row element. Their names include the 
      prefix 'autoreg:', 'boundary:' or 'initial:' to indicate their role in the simulation.
  """
  # print('rows: ', type(rows))
  # print('columns: ', type(columns))
  out = ''
  for row_idx, row in enumerate(rows):
    if row_idx==0:
      out += 'initial:'
      # print('row=', row)
      # print('columns=', columns)
      for i, c in enumerate(columns):
        # print(i,': ', i, ' row[i]=', row[i], ' c=', c)
        if c.startswith('initial:'):
         out +=' ' + str(row[i])
      out += ', '
    else:
      out += '| '
    out += 'boundary:'
    for i, c in enumerate(columns):
      if c.startswith('boundary:'):
        out +=' ' + str(row[i])
    out += ', autoreg:'
    for i, c in enumerate(columns):
      if c.startswith('autoreg:'):
        out +=' ' + str(row[i])
  out += '| boundary:'
  for i, c in enumerate(columns):
    if c.startswith('boundary:'):
      out +=' ' + str(next_row[i])

  return out
  
@dataclass
class TextTs:
  inputs: List[str]
  preds: List[str]
  max_input_len: int
  max_pred_len: int

def build_text_dataset(ts: pd.DataFrame, hist_len: int) -> TextTs:
  """Loads the simulation log dataset and generates the auto-regressive transformer training dataset.
  
  The computed dataset presents a simulation observation row as a prediction target. The context 
  for the prediction includes all the initial state variables, the autoregressive and boundary 
  variables for the preceding hist_len observations and the boundary variables for the current 
  simulation observation.

  Arguments:
    ts: DataFrame the contains the time series of all simulation runs.
    hist_len: the number of time steps to use as input for each model 
      prediction.
  
  Returns:
    The full dataset for the transformer model.
  """

  simulations = ts.groupby(['sim_location'])

  inputs = []
  preds = []
  max_input_len = 0
  max_pred_len = 0

  for _, sim_ts in simulations:
    hist = []
    data_columns = list(sim_ts.columns[3:])
    for idx in range(sim_ts.shape[0]):
      cur_row = sim_ts.iloc[idx].values.astype(str)
      if len(hist) == hist_len:
        input = generate_input(hist, cur_row[3:], data_columns)
        prediction = generate_prediction(cur_row[3:], data_columns)

        max_input_len = max(max_input_len, len(input))
        inputs.append(input)
  
        max_pred_len = max(max_pred_len, len(prediction))
        preds.append(prediction)

        if hist:
          hist.pop(0)
      hist.append(cur_row[3:]) 
  
  return TextTs(inputs, preds, max_input_len, max_pred_len)

def build_train_val_text_dataset(train_ts: pd.DataFrame, validate_ts: pd.DataFrame, hist_len: int) -> Dataset:
  """Loads the simulation log training and validation datasets and generates the corresponding auto-regressive transformer training dataset.
  
  The computed dataset presents a simulation observation row as a prediction target. The context 
  for the prediction includes all the initial state variables, the autoregressive and boundary 
  variables for the preceding hist_len observations and the boundary variables for the current 
  simulation observation.

  Arguments:
    train_ts: DataFrame the contains the time series of all training simulation runs.
    validate_ts: DataFrame the contains the time series of all training simulation runs.
    hist_len: the number of time steps to use as input for each model 
      prediction.
  
  Returns:
    The training and validation datasets for the transformner.
  """
  train = build_text_dataset(train_ts, hist_len)
  train_df = pd.DataFrame(
    {
      'input': train.inputs,
      'pred': train.preds,
    }
  )

  validate = build_text_dataset(validate_ts, hist_len)
  validate_df = pd.DataFrame(
    {
      'input': validate.inputs,
      'pred': validate.preds,
    }
  )

  return Dataset(
    train_df,
    validate_df,
    train.max_input_len + validate.max_input_len,
    train.max_pred_len + validate.max_pred_len,
  )
