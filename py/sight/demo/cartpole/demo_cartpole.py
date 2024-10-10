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
"""Demo of using the Sight Decision API to train gym environment."""

import warnings


def warn(*args, **kwargs):
  pass


warnings.warn = warn

import os
from typing import Sequence

from absl import app
from absl import flags
from acme import wrappers
import gym
from helpers.logs.logs_handler import logger as logging
import numpy as np
from sight.demo.cartpole.driver_cartpole import driver_fn
from sight.proto import sight_pb2
from sight.sight import Sight
from sight.widgets.decision import decision

FLAGS = flags.FLAGS


def get_sight_instance():
  params = sight_pb2.Params(
      label='cartpole_experiment',
      bucket_name=f'{os.environ["PROJECT_ID"]}-sight',
  )
  sight_obj = Sight(params)
  return sight_obj


def main(argv: Sequence[str]) -> None:
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")

  with get_sight_instance() as sight:
    # decision.run(sight=sight, env=wrappers.GymWrapper(gym.make("CartPole-v1")))
    decision.run(
        state_attrs={
            "Cart Position":
                sight_pb2.DecisionConfigurationStart.AttrProps(
                    min_value=-4.8,
                    max_value=4.8,
                ),
            "Cart Velocity":
                sight_pb2.DecisionConfigurationStart.AttrProps(
                    min_value=-3.40,
                    max_value=3.40,
                ),
            "Pole Angle":
                sight_pb2.DecisionConfigurationStart.AttrProps(
                    min_value=-0.418,
                    max_value=0.418,
                ),
            "Pole Angular Velocity":
                sight_pb2.DecisionConfigurationStart.AttrProps(
                    min_value=-3.40,
                    max_value=3.40,
                ),
        },
        action_attrs={
            # "direction": sight_pb2.DecisionConfigurationStart.AttrProps(
            #     valid_int_values=[0,1],
            # ),
            "direction":
                sight_pb2.DecisionConfigurationStart.AttrProps(
                    min_value=0,
                    max_value=1,
                    # step_size=1
                ),
        },
        # env=wrappers.GymWrapper(gym.make('CartPole-v1')),
        driver_fn=driver_fn,
        sight=sight,
    )


if __name__ == "__main__":
  # logging.basicConfig(level=logging.DEBUG, )
  # print(logging.getLogger(__name__))
  app.run(main)
