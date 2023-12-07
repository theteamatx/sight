# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Vizier Bayesian optimizer for driving Sight applications."""

import logging
import os
from overrides import overrides
from typing import Any, Dict, List, Tuple
from datetime import datetime
from absl import flags

from google.cloud import aiplatform
from dotenv import load_dotenv
from service import service_pb2
from service.optimizer_instance import param_dict_to_proto
from service.optimizer_instance import OptimizerInstance

load_dotenv()
# PROJECT_ID = 'catan-236106'
PROJECT_ID = os.environ['PROJECT_ID']
PROJECT_REGION = 'us-central1'
VIZIER_ENDPOINT = f'{PROJECT_REGION}-aiplatform.googleapis.com'
_vizier_client = aiplatform.gapic.VizierServiceClient(
    client_options=dict(api_endpoint=VIZIER_ENDPOINT)
)
_file_name = "vizier.py"
# FLAGS = flags.FLAGS


def _get_vizier_study_display_name(client_id: str, label: str) -> str:
  return (
      'Sight_'
      + label.replace(' ', '_')
      + '_'
      + str(client_id)
      + '_'
      + datetime.now().strftime('%Y%m%d_%H%M%S')
  )


def _get_vizier_study_config(client_id: str, label: str, study_config_param):
  """Generate a Vizier StudyConfig from command-line flags."""
  method_name = "_get_vizier_study_config"
  logging.debug(">>>>  In %s of %s", method_name, _file_name)
  study_params = []
  for attr in study_config_param.action_attrs:
    study_params.append({
        'parameter_id': attr,
        'double_value_spec': {
            'min_value': study_config_param.action_attrs[attr].min_value,
            'max_value': study_config_param.action_attrs[attr].max_value,
        },
    })
  logging.debug("<<<<  Out %s of %s", method_name, _file_name)
  return {
      'display_name': _get_vizier_study_display_name(client_id, label),
      'study_spec': {
          'algorithm': 'ALGORITHM_UNSPECIFIED',
          'parameters': study_params,
          'metrics': [{'metric_id': 'outcome', 'goal': 'MAXIMIZE'}],
      },
  }


class Vizier(OptimizerInstance):
  """Vizier specific implementation of OptimizerInstance class.
  """

  def __init__(self):
    super().__init__()
    self.vizier_study = ''
    self.current_trial: Dict[str, str] = {}

  @overrides
  def launch(
      self, request: service_pb2.LaunchRequest
  ) -> service_pb2.LaunchResponse:
    method_name = "launch"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)
    launch_response = super(Vizier, self).launch(request)

    study_config = _get_vizier_study_config(
        request.client_id, request.label, request.decision_config_params
    )
    vizier_response = _vizier_client.create_study(
        parent=f'projects/{PROJECT_ID}/locations/{PROJECT_REGION}',
        study=study_config
    )
    vizier_url = (
        'https://pantheon.corp.google.com/vertex-ai/locations/'
        + PROJECT_REGION
        + '/studies/'
        + vizier_response.name.split('/')[-1]
        + '?project='
        + PROJECT_ID
    )

    self.vizier_study = vizier_response.name
    logging.info('updated self : %s', str(self.__dict__))

    launch_response.display_string = vizier_url
    logging.debug("<<<<  Out %s of %s", method_name, _file_name)
    return launch_response

  @overrides
  def decision_point(
      self, request: service_pb2.DecisionPointRequest
  ) -> service_pb2.DecisionPointResponse:
    method_name = "decision_point"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)
    response = (
        _vizier_client.suggest_trials({
            'parent': self.vizier_study,
            'suggestion_count': 1,
            'client_id': request.worker_id,
        })
        .result()
        .trials
    )

    self.current_trial[request.worker_id] = response[0].name

    dp_response = service_pb2.DecisionPointResponse()
    dp_response.action.extend(
        param_dict_to_proto(
            {
                param.parameter_id: param.value
                for param in response[0].parameters
            }
        )
    )
    logging.debug("<<<<  Out %s of %s", method_name, _file_name)
    return dp_response

  @overrides
  def finalize_episode(
      self, request: service_pb2.FinalizeEpisodeRequest
  ) -> service_pb2.FinalizeEpisodeResponse:
    method_name = "finalize_episode"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)
    metrics = []
    metrics_obj = {}
    metrics_obj['metric_id'] = request.decision_outcome.outcome_label
    metrics_obj['value'] = request.decision_outcome.outcome_value
    metrics.append(metrics_obj)

    if request.worker_id not in self.current_trial:
      logging.info('Given worker not found......')
      logging.info('current key(worker) is  = %s', request.worker_id)
      logging.info('current instance = %s', str(self))
      return service_pb2.FinalizeEpisodeResponse(
          response_str=f'Worker {request.worker_id} has no known trial!'
      )

    logging.info('FinalizeEpisode metrics=%s', metrics)
    _vizier_client.complete_trial({
        'name': self.current_trial[request.worker_id],
        'final_measurement': {'metrics': metrics},
    })
    logging.debug("<<<<  Out %s of %s", method_name, _file_name)
    return service_pb2.FinalizeEpisodeResponse(response_str='Success!')

  @overrides
  def current_status(
      self, request: service_pb2.CurrentStatusRequest
  ) -> service_pb2.CurrentStatusResponse:
    method_name = "current_status"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)
    optimal = _vizier_client.list_optimal_trials({
        'parent': self.vizier_study,
    })
    logging.debug("<<<<  Out %s of %s", method_name, _file_name)
    return service_pb2.CurrentStatusResponse(response_str=str(optimal))
