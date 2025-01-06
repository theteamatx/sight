# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sight_service/proto/service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sight.proto import sight_pb2 as sight_dot_proto_dot_sight__pb2
from sight_service.proto.numproto.protobuf import ndarray_pb2 as sight__service_dot_proto_dot_numproto_dot_protobuf_dot_ndarray__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sight_service/proto/service.proto\x12\x0fsight.x.service\x1a\x17sight/proto/sight.proto\x1a\x33sight_service/proto/numproto/protobuf/ndarray.proto\x1a\x1cgoogle/api/annotations.proto\"\xa5\x03\n\x0c\x41\x63me_Request\x12G\n\x14\x65pisode_observations\x18\x01 \x03(\x0b\x32).sight.x.service.Acme_Request.Observation\x12\x14\n\x0clearner_keys\x18\x02 \x03(\t\x1a\xfe\x01\n\x0bObservation\x12*\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32\x1a.numproto.protobuf.NDArray\x12\x38\n\x08steptype\x18\x02 \x01(\x0e\x32&.sight.x.service.Acme_Request.StepType\x12*\n\x06reward\x18\x03 \x01(\x0b\x32\x1a.numproto.protobuf.NDArray\x12,\n\x08\x64iscount\x18\x04 \x01(\x0b\x32\x1a.numproto.protobuf.NDArray\x12/\n\x0bobservation\x18\x05 \x01(\x0b\x32\x1a.numproto.protobuf.NDArray\"5\n\x08StepType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\t\n\x05\x46IRST\x10\x01\x12\x07\n\x03MID\x10\x02\x12\x08\n\x04LAST\x10\x03\"\x80\x02\n\rAcme_Response\x12\x34\n\x06layers\x18\x01 \x03(\x0b\x32$.sight.x.service.Acme_Response.Layer\x1a\xb8\x01\n\x05Layer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x41\n\x07weights\x18\x02 \x01(\x0b\x32\x30.sight.x.service.Acme_Response.Layer.WeightsData\x1a^\n\x0bWeightsData\x12\t\n\x01\x62\x18\x01 \x03(\x02\x12%\n\x01w\x18\x02 \x01(\x0b\x32\x1a.numproto.protobuf.NDArray\x12\x0e\n\x06offset\x18\x03 \x03(\x02\x12\r\n\x05scale\x18\x04 \x03(\x02\"\xf8\x01\n\x14\x44\x65\x63isionPointRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x11\n\tworker_id\x18\x02 \x01(\t\x12\x16\n\x0equestion_label\x18\x06 \x01(\t\x12\x34\n\x0e\x64\x65\x63ision_point\x18\x03 \x01(\x0b\x32\x1c.sight.x.proto.DecisionPoint\x12\x38\n\x10\x64\x65\x63ision_outcome\x18\x04 \x01(\x0b\x32\x1e.sight.x.proto.DecisionOutcome\x12\x32\n\x0b\x61\x63me_config\x18\x05 \x01(\x0b\x32\x1d.sight.x.service.Acme_Request\"\x9f\x02\n\x15\x44\x65\x63isionPointResponse\x12,\n\x06\x61\x63tion\x18\x01 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\x12\x35\n\racme_response\x18\x02 \x01(\x0b\x32\x1e.sight.x.service.Acme_Response\x12\x14\n\x0cresponse_idx\x18\x03 \x01(\x03\x12\x46\n\x0b\x61\x63tion_type\x18\x04 \x01(\x0e\x32\x31.sight.x.service.DecisionPointResponse.ActionType\"C\n\nActionType\x12\x0e\n\nAT_UNKNOWN\x10\x00\x12\n\n\x06\x41T_ACT\x10\x01\x12\x0b\n\x07\x41T_DONE\x10\x02\x12\x0c\n\x08\x41T_RETRY\x10\x03\"A\n\x19\x46\x65tchOptimalActionRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x11\n\tworker_id\x18\x02 \x01(\t\"2\n\x1a\x46\x65tchOptimalActionResponse\x12\x14\n\x0cresponse_str\x18\x01 \x01(\t\"5\n\x0bTellRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x13\n\x0bmessage_str\x18\x02 \x01(\t\"$\n\x0cTellResponse\x12\x14\n\x0cresponse_str\x18\x01 \x01(\t\"\"\n\rListenRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\">\n\x0eListenResponse\x12\x16\n\x0eresponse_ready\x18\x01 \x01(\x08\x12\x14\n\x0cresponse_str\x18\x02 \x01(\t\"<\n\x14\x43urrentStatusRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x11\n\tworker_id\x18\x02 \x01(\t\"\xae\x01\n\x15\x43urrentStatusResponse\x12\x14\n\x0cresponse_str\x18\x01 \x01(\t\x12=\n\x06status\x18\x02 \x01(\x0e\x32-.sight.x.service.CurrentStatusResponse.Status\"@\n\x06Status\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\x12\x0b\n\x07\x46\x41ILURE\x10\x03\"\x94\x01\n\rLaunchRequest\x12I\n\x16\x64\x65\x63ision_config_params\x18\x01 \x01(\x0b\x32).sight.x.proto.DecisionConfigurationStart\x12\r\n\x05label\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t\x12\x16\n\x0equestion_label\x18\x06 \x01(\t\"(\n\x0eLaunchResponse\x12\x16\n\x0e\x64isplay_string\x18\x01 \x01(\t\"\xa7\x01\n\x14ProposeActionRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x32\n\x0c\x61\x63tion_attrs\x18\x02 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\x12\x30\n\nattributes\x18\x03 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\x12\x16\n\x0equestion_label\x18\x04 \x01(\t\"*\n\x15ProposeActionResponse\x12\x11\n\taction_id\x18\x01 \x01(\x03\"R\n\x11GetOutcomeRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x12\n\nunique_ids\x18\x02 \x03(\x03\x12\x16\n\x0equestion_label\x18\x03 \x01(\t\"\xf7\x03\n\x12GetOutcomeResponse\x12<\n\x07outcome\x18\x01 \x03(\x0b\x32+.sight.x.service.GetOutcomeResponse.Outcome\x1a\xa2\x03\n\x07Outcome\x12\x31\n\x0bstate_attrs\x18\x01 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\x12\x32\n\x0c\x61\x63tion_attrs\x18\x02 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\x12\x0e\n\x06reward\x18\x03 \x01(\x02\x12\x33\n\routcome_attrs\x18\x04 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\x12\x30\n\nattributes\x18\x05 \x03(\x0b\x32\x1c.sight.x.proto.DecisionParam\x12\x42\n\x06status\x18\x06 \x01(\x0e\x32\x32.sight.x.service.GetOutcomeResponse.Outcome.Status\x12\x14\n\x0cresponse_str\x18\x07 \x01(\t\x12\x11\n\taction_id\x18\x08 \x01(\x03\"L\n\x06Status\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\r\n\tCOMPLETED\x10\x03\x12\r\n\tNOT_EXIST\x10\x04\"\xcb\x02\n\x16\x46inalizeEpisodeRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x11\n\tworker_id\x18\x02 \x01(\t\x12\x16\n\x0equestion_label\x18\x07 \x01(\t\x12\x34\n\x0e\x64\x65\x63ision_point\x18\x03 \x01(\x0b\x32\x1c.sight.x.proto.DecisionPoint\x12\x38\n\x10\x64\x65\x63ision_outcome\x18\x04 \x01(\x0b\x32\x1e.sight.x.proto.DecisionOutcome\x12O\n\x0eoptimizer_type\x18\x05 \x01(\x0e\x32\x37.sight.x.proto.DecisionConfigurationStart.OptimizerType\x12\x32\n\x0b\x61\x63me_config\x18\x06 \x01(\x0b\x32\x1d.sight.x.service.Acme_Request\"D\n\x17\x46inalizeEpisodeResponse\x12\x14\n\x0cresponse_str\x18\x01 \x01(\t\x12\x13\n\x0bstop_worker\x18\x02 \x01(\x08\" \n\x0bTestRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\"\x1b\n\x0cTestResponse\x12\x0b\n\x03val\x18\x01 \x01(\t\"\x0f\n\rCreateRequest\"1\n\x0e\x43reateResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0bpath_prefix\x18\x02 \x01(\t\"!\n\x0c\x43loseRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\"%\n\rCloseResponse\x12\x14\n\x0cresponse_str\x18\x01 \x01(\t\"R\n\x12WorkerAliveRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x11\n\tworker_id\x18\x02 \x01(\t\x12\x16\n\x0equestion_label\x18\x04 \x01(\t\"\xa0\x01\n\x13WorkerAliveResponse\x12\x44\n\x0bstatus_type\x18\x04 \x01(\x0e\x32/.sight.x.service.WorkerAliveResponse.StatusType\"C\n\nStatusType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\n\n\x06ST_ACT\x10\x01\x12\x0b\n\x07ST_DONE\x10\x02\x12\x0c\n\x08ST_RETRY\x10\x03*[\n\tLogFormat\x12\x0e\n\nLF_UNKNOWN\x10\x00\x12\x0f\n\x0bLF_COLUMNIO\x10\x01\x12\x10\n\x0cLF_CAPACITOR\x10\x02\x12\x0e\n\nLF_SPANNER\x10\x03\x12\x0b\n\x07LF_AVRO\x10\x04\x32\xd6\x0c\n\x0cSightService\x12\x61\n\x04Test\x12\x1c.sight.x.service.TestRequest\x1a\x1d.sight.x.service.TestResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/test/{client_id}\x12]\n\x06\x43reate\x12\x1e.sight.x.service.CreateRequest\x1a\x1f.sight.x.service.CreateResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/create\x12Y\n\x05\x43lose\x12\x1d.sight.x.service.CloseRequest\x1a\x1e.sight.x.service.CloseResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/v1/Close\x12q\n\x0bWorkerAlive\x12#.sight.x.service.WorkerAliveRequest\x1a$.sight.x.service.WorkerAliveResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/WorkerAlive\x12\x89\x01\n\x06Launch\x12\x1e.sight.x.service.LaunchRequest\x1a\x1f.sight.x.service.LaunchResponse\">\x82\xd3\xe4\x93\x02\x38\"\x1e/v1/launch/{client_id}/{label}:\x16\x64\x65\x63ision_config_params\x12\x9f\x01\n\rDecisionPoint\x12%.sight.x.service.DecisionPointRequest\x1a&.sight.x.service.DecisionPointResponse\"?\x82\xd3\xe4\x93\x02\x39\"*/v1/decision_point/{client_id}/{worker_id}:\x0b\x61\x63me_config\x12m\n\x04Tell\x12\x1c.sight.x.service.TellRequest\x1a\x1d.sight.x.service.TellResponse\"(\x82\xd3\xe4\x93\x02\"\" /v1/tell/{client_id}/{worker_id}\x12u\n\x06Listen\x12\x1e.sight.x.service.ListenRequest\x1a\x1f.sight.x.service.ListenResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/v1/listen/{client_id}/{worker_id}\x12\x92\x01\n\rCurrentStatus\x12%.sight.x.service.CurrentStatusRequest\x1a&.sight.x.service.CurrentStatusResponse\"2\x82\xd3\xe4\x93\x02,\x12*/v1/current_status/{client_id}/{worker_id}\x12\xa7\x01\n\x12\x46\x65tchOptimalAction\x12*.sight.x.service.FetchOptimalActionRequest\x1a+.sight.x.service.FetchOptimalActionResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/v1/fetch_optimal_action/{client_id}/{worker_id}\x12`\n\rProposeAction\x12%.sight.x.service.ProposeActionRequest\x1a&.sight.x.service.ProposeActionResponse\"\x00\x12W\n\nGetOutcome\x12\".sight.x.service.GetOutcomeRequest\x1a#.sight.x.service.GetOutcomeResponse\"\x00\x12\xa7\x01\n\x0f\x46inalizeEpisode\x12\'.sight.x.service.FinalizeEpisodeRequest\x1a(.sight.x.service.FinalizeEpisodeResponse\"A\x82\xd3\xe4\x93\x02;\",/v1/finalize_episode/{client_id}/{worker_id}:\x0b\x61\x63me_configb\x06proto3')

_LOGFORMAT = DESCRIPTOR.enum_types_by_name['LogFormat']
LogFormat = enum_type_wrapper.EnumTypeWrapper(_LOGFORMAT)
LF_UNKNOWN = 0
LF_COLUMNIO = 1
LF_CAPACITOR = 2
LF_SPANNER = 3
LF_AVRO = 4


_ACME_REQUEST = DESCRIPTOR.message_types_by_name['Acme_Request']
_ACME_REQUEST_OBSERVATION = _ACME_REQUEST.nested_types_by_name['Observation']
_ACME_RESPONSE = DESCRIPTOR.message_types_by_name['Acme_Response']
_ACME_RESPONSE_LAYER = _ACME_RESPONSE.nested_types_by_name['Layer']
_ACME_RESPONSE_LAYER_WEIGHTSDATA = _ACME_RESPONSE_LAYER.nested_types_by_name['WeightsData']
_DECISIONPOINTREQUEST = DESCRIPTOR.message_types_by_name['DecisionPointRequest']
_DECISIONPOINTRESPONSE = DESCRIPTOR.message_types_by_name['DecisionPointResponse']
_FETCHOPTIMALACTIONREQUEST = DESCRIPTOR.message_types_by_name['FetchOptimalActionRequest']
_FETCHOPTIMALACTIONRESPONSE = DESCRIPTOR.message_types_by_name['FetchOptimalActionResponse']
_TELLREQUEST = DESCRIPTOR.message_types_by_name['TellRequest']
_TELLRESPONSE = DESCRIPTOR.message_types_by_name['TellResponse']
_LISTENREQUEST = DESCRIPTOR.message_types_by_name['ListenRequest']
_LISTENRESPONSE = DESCRIPTOR.message_types_by_name['ListenResponse']
_CURRENTSTATUSREQUEST = DESCRIPTOR.message_types_by_name['CurrentStatusRequest']
_CURRENTSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['CurrentStatusResponse']
_LAUNCHREQUEST = DESCRIPTOR.message_types_by_name['LaunchRequest']
_LAUNCHRESPONSE = DESCRIPTOR.message_types_by_name['LaunchResponse']
_PROPOSEACTIONREQUEST = DESCRIPTOR.message_types_by_name['ProposeActionRequest']
_PROPOSEACTIONRESPONSE = DESCRIPTOR.message_types_by_name['ProposeActionResponse']
_GETOUTCOMEREQUEST = DESCRIPTOR.message_types_by_name['GetOutcomeRequest']
_GETOUTCOMERESPONSE = DESCRIPTOR.message_types_by_name['GetOutcomeResponse']
_GETOUTCOMERESPONSE_OUTCOME = _GETOUTCOMERESPONSE.nested_types_by_name['Outcome']
_FINALIZEEPISODEREQUEST = DESCRIPTOR.message_types_by_name['FinalizeEpisodeRequest']
_FINALIZEEPISODERESPONSE = DESCRIPTOR.message_types_by_name['FinalizeEpisodeResponse']
_TESTREQUEST = DESCRIPTOR.message_types_by_name['TestRequest']
_TESTRESPONSE = DESCRIPTOR.message_types_by_name['TestResponse']
_CREATEREQUEST = DESCRIPTOR.message_types_by_name['CreateRequest']
_CREATERESPONSE = DESCRIPTOR.message_types_by_name['CreateResponse']
_CLOSEREQUEST = DESCRIPTOR.message_types_by_name['CloseRequest']
_CLOSERESPONSE = DESCRIPTOR.message_types_by_name['CloseResponse']
_WORKERALIVEREQUEST = DESCRIPTOR.message_types_by_name['WorkerAliveRequest']
_WORKERALIVERESPONSE = DESCRIPTOR.message_types_by_name['WorkerAliveResponse']
_ACME_REQUEST_STEPTYPE = _ACME_REQUEST.enum_types_by_name['StepType']
_DECISIONPOINTRESPONSE_ACTIONTYPE = _DECISIONPOINTRESPONSE.enum_types_by_name['ActionType']
_CURRENTSTATUSRESPONSE_STATUS = _CURRENTSTATUSRESPONSE.enum_types_by_name['Status']
_GETOUTCOMERESPONSE_OUTCOME_STATUS = _GETOUTCOMERESPONSE_OUTCOME.enum_types_by_name['Status']
_WORKERALIVERESPONSE_STATUSTYPE = _WORKERALIVERESPONSE.enum_types_by_name['StatusType']
Acme_Request = _reflection.GeneratedProtocolMessageType('Acme_Request', (_message.Message,), {

  'Observation' : _reflection.GeneratedProtocolMessageType('Observation', (_message.Message,), {
    'DESCRIPTOR' : _ACME_REQUEST_OBSERVATION,
    '__module__' : 'sight_service.proto.service_pb2'
    # @@protoc_insertion_point(class_scope:sight.x.service.Acme_Request.Observation)
    })
  ,
  'DESCRIPTOR' : _ACME_REQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.Acme_Request)
  })
_sym_db.RegisterMessage(Acme_Request)
_sym_db.RegisterMessage(Acme_Request.Observation)

Acme_Response = _reflection.GeneratedProtocolMessageType('Acme_Response', (_message.Message,), {

  'Layer' : _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), {

    'WeightsData' : _reflection.GeneratedProtocolMessageType('WeightsData', (_message.Message,), {
      'DESCRIPTOR' : _ACME_RESPONSE_LAYER_WEIGHTSDATA,
      '__module__' : 'sight_service.proto.service_pb2'
      # @@protoc_insertion_point(class_scope:sight.x.service.Acme_Response.Layer.WeightsData)
      })
    ,
    'DESCRIPTOR' : _ACME_RESPONSE_LAYER,
    '__module__' : 'sight_service.proto.service_pb2'
    # @@protoc_insertion_point(class_scope:sight.x.service.Acme_Response.Layer)
    })
  ,
  'DESCRIPTOR' : _ACME_RESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.Acme_Response)
  })
_sym_db.RegisterMessage(Acme_Response)
_sym_db.RegisterMessage(Acme_Response.Layer)
_sym_db.RegisterMessage(Acme_Response.Layer.WeightsData)

DecisionPointRequest = _reflection.GeneratedProtocolMessageType('DecisionPointRequest', (_message.Message,), {
  'DESCRIPTOR' : _DECISIONPOINTREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.DecisionPointRequest)
  })
_sym_db.RegisterMessage(DecisionPointRequest)

DecisionPointResponse = _reflection.GeneratedProtocolMessageType('DecisionPointResponse', (_message.Message,), {
  'DESCRIPTOR' : _DECISIONPOINTRESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.DecisionPointResponse)
  })
_sym_db.RegisterMessage(DecisionPointResponse)

FetchOptimalActionRequest = _reflection.GeneratedProtocolMessageType('FetchOptimalActionRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHOPTIMALACTIONREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.FetchOptimalActionRequest)
  })
_sym_db.RegisterMessage(FetchOptimalActionRequest)

FetchOptimalActionResponse = _reflection.GeneratedProtocolMessageType('FetchOptimalActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHOPTIMALACTIONRESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.FetchOptimalActionResponse)
  })
_sym_db.RegisterMessage(FetchOptimalActionResponse)

TellRequest = _reflection.GeneratedProtocolMessageType('TellRequest', (_message.Message,), {
  'DESCRIPTOR' : _TELLREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.TellRequest)
  })
_sym_db.RegisterMessage(TellRequest)

TellResponse = _reflection.GeneratedProtocolMessageType('TellResponse', (_message.Message,), {
  'DESCRIPTOR' : _TELLRESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.TellResponse)
  })
_sym_db.RegisterMessage(TellResponse)

ListenRequest = _reflection.GeneratedProtocolMessageType('ListenRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTENREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.ListenRequest)
  })
_sym_db.RegisterMessage(ListenRequest)

ListenResponse = _reflection.GeneratedProtocolMessageType('ListenResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTENRESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.ListenResponse)
  })
_sym_db.RegisterMessage(ListenResponse)

CurrentStatusRequest = _reflection.GeneratedProtocolMessageType('CurrentStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _CURRENTSTATUSREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.CurrentStatusRequest)
  })
_sym_db.RegisterMessage(CurrentStatusRequest)

CurrentStatusResponse = _reflection.GeneratedProtocolMessageType('CurrentStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _CURRENTSTATUSRESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.CurrentStatusResponse)
  })
_sym_db.RegisterMessage(CurrentStatusResponse)

LaunchRequest = _reflection.GeneratedProtocolMessageType('LaunchRequest', (_message.Message,), {
  'DESCRIPTOR' : _LAUNCHREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.LaunchRequest)
  })
_sym_db.RegisterMessage(LaunchRequest)

LaunchResponse = _reflection.GeneratedProtocolMessageType('LaunchResponse', (_message.Message,), {
  'DESCRIPTOR' : _LAUNCHRESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.LaunchResponse)
  })
_sym_db.RegisterMessage(LaunchResponse)

ProposeActionRequest = _reflection.GeneratedProtocolMessageType('ProposeActionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSEACTIONREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.ProposeActionRequest)
  })
_sym_db.RegisterMessage(ProposeActionRequest)

ProposeActionResponse = _reflection.GeneratedProtocolMessageType('ProposeActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSEACTIONRESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.ProposeActionResponse)
  })
_sym_db.RegisterMessage(ProposeActionResponse)

GetOutcomeRequest = _reflection.GeneratedProtocolMessageType('GetOutcomeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOUTCOMEREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.GetOutcomeRequest)
  })
_sym_db.RegisterMessage(GetOutcomeRequest)

GetOutcomeResponse = _reflection.GeneratedProtocolMessageType('GetOutcomeResponse', (_message.Message,), {

  'Outcome' : _reflection.GeneratedProtocolMessageType('Outcome', (_message.Message,), {
    'DESCRIPTOR' : _GETOUTCOMERESPONSE_OUTCOME,
    '__module__' : 'sight_service.proto.service_pb2'
    # @@protoc_insertion_point(class_scope:sight.x.service.GetOutcomeResponse.Outcome)
    })
  ,
  'DESCRIPTOR' : _GETOUTCOMERESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.GetOutcomeResponse)
  })
_sym_db.RegisterMessage(GetOutcomeResponse)
_sym_db.RegisterMessage(GetOutcomeResponse.Outcome)

FinalizeEpisodeRequest = _reflection.GeneratedProtocolMessageType('FinalizeEpisodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZEEPISODEREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.FinalizeEpisodeRequest)
  })
_sym_db.RegisterMessage(FinalizeEpisodeRequest)

FinalizeEpisodeResponse = _reflection.GeneratedProtocolMessageType('FinalizeEpisodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZEEPISODERESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.FinalizeEpisodeResponse)
  })
_sym_db.RegisterMessage(FinalizeEpisodeResponse)

TestRequest = _reflection.GeneratedProtocolMessageType('TestRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.TestRequest)
  })
_sym_db.RegisterMessage(TestRequest)

TestResponse = _reflection.GeneratedProtocolMessageType('TestResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.TestResponse)
  })
_sym_db.RegisterMessage(TestResponse)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATERESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.CreateResponse)
  })
_sym_db.RegisterMessage(CreateResponse)

CloseRequest = _reflection.GeneratedProtocolMessageType('CloseRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSEREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.CloseRequest)
  })
_sym_db.RegisterMessage(CloseRequest)

CloseResponse = _reflection.GeneratedProtocolMessageType('CloseResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSERESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.CloseResponse)
  })
_sym_db.RegisterMessage(CloseResponse)

WorkerAliveRequest = _reflection.GeneratedProtocolMessageType('WorkerAliveRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKERALIVEREQUEST,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.WorkerAliveRequest)
  })
_sym_db.RegisterMessage(WorkerAliveRequest)

WorkerAliveResponse = _reflection.GeneratedProtocolMessageType('WorkerAliveResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKERALIVERESPONSE,
  '__module__' : 'sight_service.proto.service_pb2'
  # @@protoc_insertion_point(class_scope:sight.x.service.WorkerAliveResponse)
  })
_sym_db.RegisterMessage(WorkerAliveResponse)

_SIGHTSERVICE = DESCRIPTOR.services_by_name['SightService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIGHTSERVICE.methods_by_name['Test']._options = None
  _SIGHTSERVICE.methods_by_name['Test']._serialized_options = b'\202\323\344\223\002\026\022\024/v1/test/{client_id}'
  _SIGHTSERVICE.methods_by_name['Create']._options = None
  _SIGHTSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\014\022\n/v1/create'
  _SIGHTSERVICE.methods_by_name['Close']._options = None
  _SIGHTSERVICE.methods_by_name['Close']._serialized_options = b'\202\323\344\223\002\013\022\t/v1/Close'
  _SIGHTSERVICE.methods_by_name['WorkerAlive']._options = None
  _SIGHTSERVICE.methods_by_name['WorkerAlive']._serialized_options = b'\202\323\344\223\002\021\022\017/v1/WorkerAlive'
  _SIGHTSERVICE.methods_by_name['Launch']._options = None
  _SIGHTSERVICE.methods_by_name['Launch']._serialized_options = b'\202\323\344\223\0028\"\036/v1/launch/{client_id}/{label}:\026decision_config_params'
  _SIGHTSERVICE.methods_by_name['DecisionPoint']._options = None
  _SIGHTSERVICE.methods_by_name['DecisionPoint']._serialized_options = b'\202\323\344\223\0029\"*/v1/decision_point/{client_id}/{worker_id}:\013acme_config'
  _SIGHTSERVICE.methods_by_name['Tell']._options = None
  _SIGHTSERVICE.methods_by_name['Tell']._serialized_options = b'\202\323\344\223\002\"\" /v1/tell/{client_id}/{worker_id}'
  _SIGHTSERVICE.methods_by_name['Listen']._options = None
  _SIGHTSERVICE.methods_by_name['Listen']._serialized_options = b'\202\323\344\223\002$\022\"/v1/listen/{client_id}/{worker_id}'
  _SIGHTSERVICE.methods_by_name['CurrentStatus']._options = None
  _SIGHTSERVICE.methods_by_name['CurrentStatus']._serialized_options = b'\202\323\344\223\002,\022*/v1/current_status/{client_id}/{worker_id}'
  _SIGHTSERVICE.methods_by_name['FetchOptimalAction']._options = None
  _SIGHTSERVICE.methods_by_name['FetchOptimalAction']._serialized_options = b'\202\323\344\223\0022\0220/v1/fetch_optimal_action/{client_id}/{worker_id}'
  _SIGHTSERVICE.methods_by_name['FinalizeEpisode']._options = None
  _SIGHTSERVICE.methods_by_name['FinalizeEpisode']._serialized_options = b'\202\323\344\223\002;\",/v1/finalize_episode/{client_id}/{worker_id}:\013acme_config'
  _LOGFORMAT._serialized_start=3790
  _LOGFORMAT._serialized_end=3881
  _ACME_REQUEST._serialized_start=163
  _ACME_REQUEST._serialized_end=584
  _ACME_REQUEST_OBSERVATION._serialized_start=275
  _ACME_REQUEST_OBSERVATION._serialized_end=529
  _ACME_REQUEST_STEPTYPE._serialized_start=531
  _ACME_REQUEST_STEPTYPE._serialized_end=584
  _ACME_RESPONSE._serialized_start=587
  _ACME_RESPONSE._serialized_end=843
  _ACME_RESPONSE_LAYER._serialized_start=659
  _ACME_RESPONSE_LAYER._serialized_end=843
  _ACME_RESPONSE_LAYER_WEIGHTSDATA._serialized_start=749
  _ACME_RESPONSE_LAYER_WEIGHTSDATA._serialized_end=843
  _DECISIONPOINTREQUEST._serialized_start=846
  _DECISIONPOINTREQUEST._serialized_end=1094
  _DECISIONPOINTRESPONSE._serialized_start=1097
  _DECISIONPOINTRESPONSE._serialized_end=1384
  _DECISIONPOINTRESPONSE_ACTIONTYPE._serialized_start=1317
  _DECISIONPOINTRESPONSE_ACTIONTYPE._serialized_end=1384
  _FETCHOPTIMALACTIONREQUEST._serialized_start=1386
  _FETCHOPTIMALACTIONREQUEST._serialized_end=1451
  _FETCHOPTIMALACTIONRESPONSE._serialized_start=1453
  _FETCHOPTIMALACTIONRESPONSE._serialized_end=1503
  _TELLREQUEST._serialized_start=1505
  _TELLREQUEST._serialized_end=1558
  _TELLRESPONSE._serialized_start=1560
  _TELLRESPONSE._serialized_end=1596
  _LISTENREQUEST._serialized_start=1598
  _LISTENREQUEST._serialized_end=1632
  _LISTENRESPONSE._serialized_start=1634
  _LISTENRESPONSE._serialized_end=1696
  _CURRENTSTATUSREQUEST._serialized_start=1698
  _CURRENTSTATUSREQUEST._serialized_end=1758
  _CURRENTSTATUSRESPONSE._serialized_start=1761
  _CURRENTSTATUSRESPONSE._serialized_end=1935
  _CURRENTSTATUSRESPONSE_STATUS._serialized_start=1871
  _CURRENTSTATUSRESPONSE_STATUS._serialized_end=1935
  _LAUNCHREQUEST._serialized_start=1938
  _LAUNCHREQUEST._serialized_end=2086
  _LAUNCHRESPONSE._serialized_start=2088
  _LAUNCHRESPONSE._serialized_end=2128
  _PROPOSEACTIONREQUEST._serialized_start=2131
  _PROPOSEACTIONREQUEST._serialized_end=2298
  _PROPOSEACTIONRESPONSE._serialized_start=2300
  _PROPOSEACTIONRESPONSE._serialized_end=2342
  _GETOUTCOMEREQUEST._serialized_start=2344
  _GETOUTCOMEREQUEST._serialized_end=2426
  _GETOUTCOMERESPONSE._serialized_start=2429
  _GETOUTCOMERESPONSE._serialized_end=2932
  _GETOUTCOMERESPONSE_OUTCOME._serialized_start=2514
  _GETOUTCOMERESPONSE_OUTCOME._serialized_end=2932
  _GETOUTCOMERESPONSE_OUTCOME_STATUS._serialized_start=2856
  _GETOUTCOMERESPONSE_OUTCOME_STATUS._serialized_end=2932
  _FINALIZEEPISODEREQUEST._serialized_start=2935
  _FINALIZEEPISODEREQUEST._serialized_end=3266
  _FINALIZEEPISODERESPONSE._serialized_start=3268
  _FINALIZEEPISODERESPONSE._serialized_end=3336
  _TESTREQUEST._serialized_start=3338
  _TESTREQUEST._serialized_end=3370
  _TESTRESPONSE._serialized_start=3372
  _TESTRESPONSE._serialized_end=3399
  _CREATEREQUEST._serialized_start=3401
  _CREATEREQUEST._serialized_end=3416
  _CREATERESPONSE._serialized_start=3418
  _CREATERESPONSE._serialized_end=3467
  _CLOSEREQUEST._serialized_start=3469
  _CLOSEREQUEST._serialized_end=3502
  _CLOSERESPONSE._serialized_start=3504
  _CLOSERESPONSE._serialized_end=3541
  _WORKERALIVEREQUEST._serialized_start=3543
  _WORKERALIVEREQUEST._serialized_end=3625
  _WORKERALIVERESPONSE._serialized_start=3628
  _WORKERALIVERESPONSE._serialized_end=3788
  _WORKERALIVERESPONSE_STATUSTYPE._serialized_start=3721
  _WORKERALIVERESPONSE_STATUSTYPE._serialized_end=3788
  _SIGHTSERVICE._serialized_start=3884
  _SIGHTSERVICE._serialized_end=5506
# @@protoc_insertion_point(module_scope)
