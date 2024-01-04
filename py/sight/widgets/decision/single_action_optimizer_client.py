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

"""Client for optimizers that are called once per episode to communicate with server."""
from typing import Optional, Sequence, Tuple
from sight_service.proto import service_pb2
from sight import service_utils as service
from sight.proto import sight_pb2
from sight.widgets.decision.optimizer_client import OptimizerClient
from overrides import override


class SingleActionOptimizerClient(OptimizerClient):
  """Single-action Client for the Sight service."""

  def __init__(self, optimizer_type: sight_pb2.DecisionConfigurationStart.OptimizerType, sight):
    super().__init__(optimizer_type)
    self._sight = sight

  @override
  def decision_point(self, sight, request: service_pb2.DecisionPointRequest):
    response = service.call(
        lambda s, meta: s.DecisionPoint(request, 300, metadata=meta)
    )
    print("response: ",response)

    return self._get_dp_action(response)

  @override
  def finalize_episode(self, sight, request: service_pb2.FinalizeEpisodeRequest):
    response = service.call(
        lambda s, meta: s.FinalizeEpisode(request, 300, metadata=meta)
    )
    return response
