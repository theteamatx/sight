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
"""Exhaustive search for driving Sight applications."""

import threading
from typing import Any, Dict, List, Tuple

from helpers.logs.logs_handler import logger as logging
from overrides import overrides
from readerwriterlock import rwlock
from sight.proto import sight_pb2
from sight.widgets.decision import utils
# from sight_service.optimizer_instance import OptimizerInstance
from sight_service.optimizer_instance import param_dict_to_proto
from sight_service.optimizer_instance import param_proto_to_dict
from sight_service.proto import service_pb2
from sight_service.single_action_optimizer import SingleActionOptimizer

_file_name = "exhaustive_search.py"


class WorklistScheduler(SingleActionOptimizer):
  """Exhaustively searches over all the possible values of the action attributes.

  Attributes:
    possible_values: Maps each action attributes to the list of possible values
      of this attribute.
  """

  def __init__(self):
    super().__init__()
    self.next_sample_to_issue = []
    self.last_sample = False
    self.exp_completed = False
    self.possible_values = {}
    self.max_reward_sample = {}

  @overrides
  def launch(self,
             request: service_pb2.LaunchRequest) -> service_pb2.LaunchResponse:
    method_name = "launch"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)
    response = super(WorklistScheduler, self).launch(request)
    response.display_string = 'Worklist Scheduler SUCCESS!'
    logging.debug("<<<<  Out %s of %s", method_name, _file_name)
    return response

  @overrides
  def propose_action(
      self, request: service_pb2.ProposeActionRequest
    ) -> service_pb2.ProposeActionResponse:
    # print('request in propose actions: ', request)

    attributes = param_proto_to_dict(request.attributes)
    action_attrs = param_proto_to_dict(request.action_attrs)

    unique_id = self.queue.push_message(message={
        "action_atrrs": action_attrs,
        "attributes": attributes
    })

    logging.info("self.queue => %s", self.queue)

    response = service_pb2.ProposeActionResponse(action_id=unique_id)
    return response

  @overrides
  def GetOutcome(
      self,
      request: service_pb2.GetOutcomeRequest) -> service_pb2.GetOutcomeResponse:

    logging.info('self.queue => %s', self.queue)

    all_messages = self.queue.get_all_messages()

    response = service_pb2.GetOutcomeResponse()
    if not request.unique_ids:
      for sample_id in all_messages["completed"]:
        sample_details = all_messages["completed"][sample_id]
        outcome = response.outcome.add()
        outcome.action_id = sample_id
        outcome.status = service_pb2.GetOutcomeResponse.Outcome.Status.COMPLETED
        outcome.reward = sample_details['reward']
        outcome.action_atrrs.extend(
            param_dict_to_proto(sample_details['action']))
        outcome.outcome_attrs.extend(
            param_dict_to_proto(sample_details['outcome']))
        outcome.attributes.extend(
            param_dict_to_proto(sample_details['attribute']))
    else:
      required_samples = list(request.unique_ids)
      for sample_id in required_samples:
        outcome = response.outcome.add()
        outcome.action_id = sample_id
        if sample_id in all_messages['completed']:
          sample_details = all_messages['completed'][sample_id]
          outcome.status = service_pb2.GetOutcomeResponse.Outcome.Status.COMPLETED
          outcome.reward = sample_details['reward']
          outcome.action_attrs.extend(
              param_dict_to_proto(sample_details['action']))
          outcome.outcome_attrs.extend(
              param_dict_to_proto(sample_details['outcome']))
          outcome.attributes.extend(
              param_dict_to_proto(sample_details['attribute']))
        elif sample_id in all_messages['pending']:
          outcome.status = service_pb2.GetOutcomeResponse.Outcome.Status.PENDING
          outcome.response_str = '!! requested sample not yet assigned to any worker !!'
        elif sample_id in all_messages['active']:
          outcome.status = service_pb2.GetOutcomeResponse.Outcome.Status.ACTIVE
          outcome.response_str = '!! requested sample not completed yet !!'
        else:
          outcome.status = service_pb2.GetOutcomeResponse.Outcome.Status.NOT_EXIST
          outcome.response_str = f'!! requested sample Id {sample_id} does not exist !!'
    return response

  @overrides
  def decision_point(
      self, request: service_pb2.DecisionPointRequest
    ) -> service_pb2.DecisionPointResponse:
    method_name = "decision_point"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)
    logging.info('seld.queue ==> %s', self.queue)

    all_messages = self.queue.get_all_messages()

    response = service_pb2.DecisionPointResponse()
    if request.worker_id in all_messages['active']:
      samples = all_messages['active'][request.worker_id]
    else:
      raise ValueError("Key not found in active_samples")
    next_action = list(samples.values())[0]["action_atrrs"]
    logging.info('next_action=%s', next_action)
    response.action.extend(param_dict_to_proto(next_action))
    response.action_type = service_pb2.DecisionPointResponse.ActionType.AT_ACT
    logging.debug("<<<<  Out %s of %s", method_name, _file_name)
    return response

    # --- end

    # dp_response = service_pb2.DecisionPointResponse()
    # if(self.exp_completed):
    #   logging.info("sight experiment completed, killing the worker")
    #   dp_response.action_type = service_pb2.DecisionPointResponse.ActionType.AT_DONE
    # else:
    # if self.pending_samples:

    # todo : meetashah : add logic to fetch action stored from propose actions and send it as repsonse
    # key, sample = self.pending_samples.popitem()
    # fetching the key in FIFO manner

    #? this part now handled by worker alive rpc
    # with self.pending_lock.gen_wlock():
    #   key = next(iter(self.pending_samples))
    #   sample = self.pending_samples.pop(key)

    # with self.active_lock.gen_wlock():
    #   self.active_samples[request.worker_id] = {'id': key, 'sample': sample}

    # with self.active_lock.gen_rlock():
    #     if (request.worker_id in self.active_samples):
    #         sample = self.active_samples[request.worker_id]['sample']
    #     else:
    #         raise ValueError("key not foung in active_samples")
    # next_action = sample[0]
    # logging.info('next_action=%s', next_action)
    # # raise SystemExit
    # dp_response.action.extend(param_dict_to_proto(next_action))
    # dp_response.action_type = service_pb2.DecisionPointResponse.ActionType.AT_ACT
    # logging.debug("<<<<  Out %s of %s", method_name, _file_name)
    # return dp_response

  @overrides
  def finalize_episode(
      self, request: service_pb2.FinalizeEpisodeRequest
    ) -> service_pb2.FinalizeEpisodeResponse:
    method_name = "finalize_episode"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)

    logging.info("self.queue => %s", self.queue)

    all_messages = self.queue.get_all_messages()

    active_messages = all_messages["active"][request.worker_id]

    for action_id, message in active_messages.items():
      self.queue.complete_message(
          message_id=action_id,
          worker_id=request.worker_id,
          extra_details={
              'action':
                  param_proto_to_dict(request.decision_point.choice_params),
              'attribute':
                  message["attributes"],
              'reward':
                  request.decision_outcome.reward,
              'outcome':
                  param_proto_to_dict(request.decision_outcome.outcome_params)
          })

    logging.info("self.queue => %s", self.queue)

    logging.debug("<<<<  Out %s of %s", method_name, _file_name)
    return service_pb2.FinalizeEpisodeResponse(response_str='Success!')

  @overrides
  def current_status(
      self, request: service_pb2.CurrentStatusRequest
    ) -> service_pb2.CurrentStatusResponse:
    method_name = "current_status"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)
    # add logic to check status - ref from exhaustive search

  @overrides
  def fetch_optimal_action(
      self, request: service_pb2.FetchOptimalActionRequest
    ) -> service_pb2.FetchOptimalActionResponse:
    method_name = "fetch_optimal_action"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)
    # add logic to check status - ref from exhaustive search
    logging.debug("<<<<  Out %s of %s", method_name, _file_name)

  @overrides
  def close(self,
            request: service_pb2.CloseRequest) -> service_pb2.CloseResponse:
    method_name = "close"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)
    self.exp_completed = True
    logging.info(
        "sight experiment completed...., changed exp_completed to True")
    logging.debug("<<<<  Out %s of %s", method_name, _file_name)
    return service_pb2.CloseResponse(response_str="success")

  @overrides
  def WorkerAlive(
      self, request: service_pb2.WorkerAliveRequest
    ) -> service_pb2.WorkerAliveResponse:
    method_name = "WorkerAlive"
    logging.debug(">>>>  In %s of %s", method_name, _file_name)

    logging.info("self.queue => %s", self.queue)

    all_messages = self.queue.get_all_messages()

    if (self.exp_completed):
      worker_alive_status = service_pb2.WorkerAliveResponse.StatusType.ST_DONE
    elif (not all_messages['pending']):
      worker_alive_status = service_pb2.WorkerAliveResponse.StatusType.ST_RETRY
    else:
      worker_alive_status = service_pb2.WorkerAliveResponse.StatusType.ST_ACT

      self.queue.process_messages(worker_id=request.worker_id)

    logging.info("self.queue => %s", self.queue)
    logging.info("worker_alive_status is %s", worker_alive_status)
    logging.debug("<<<<  Out %s of %s", method_name, _file_name)
    return service_pb2.WorkerAliveResponse(status_type=worker_alive_status)
