# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sight_service.proto import service_pb2 as sight__service_dot_proto_dot_service__pb2


class SightServiceStub(object):
    """This API manages Sight logs, their creation and access to them.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Test = channel.unary_unary(
                '/sight.x.service.SightService/Test',
                request_serializer=sight__service_dot_proto_dot_service__pb2.TestRequest.SerializeToString,
                response_deserializer=sight__service_dot_proto_dot_service__pb2.TestResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/sight.x.service.SightService/Create',
                request_serializer=sight__service_dot_proto_dot_service__pb2.CreateRequest.SerializeToString,
                response_deserializer=sight__service_dot_proto_dot_service__pb2.CreateResponse.FromString,
                )
        self.Launch = channel.unary_unary(
                '/sight.x.service.SightService/Launch',
                request_serializer=sight__service_dot_proto_dot_service__pb2.LaunchRequest.SerializeToString,
                response_deserializer=sight__service_dot_proto_dot_service__pb2.LaunchResponse.FromString,
                )
        self.DecisionPoint = channel.unary_unary(
                '/sight.x.service.SightService/DecisionPoint',
                request_serializer=sight__service_dot_proto_dot_service__pb2.DecisionPointRequest.SerializeToString,
                response_deserializer=sight__service_dot_proto_dot_service__pb2.DecisionPointResponse.FromString,
                )
        self.Tell = channel.unary_unary(
                '/sight.x.service.SightService/Tell',
                request_serializer=sight__service_dot_proto_dot_service__pb2.TellRequest.SerializeToString,
                response_deserializer=sight__service_dot_proto_dot_service__pb2.TellResponse.FromString,
                )
        self.Listen = channel.unary_unary(
                '/sight.x.service.SightService/Listen',
                request_serializer=sight__service_dot_proto_dot_service__pb2.ListenRequest.SerializeToString,
                response_deserializer=sight__service_dot_proto_dot_service__pb2.ListenResponse.FromString,
                )
        self.CurrentStatus = channel.unary_unary(
                '/sight.x.service.SightService/CurrentStatus',
                request_serializer=sight__service_dot_proto_dot_service__pb2.CurrentStatusRequest.SerializeToString,
                response_deserializer=sight__service_dot_proto_dot_service__pb2.CurrentStatusResponse.FromString,
                )
        self.FetchOptimalAction = channel.unary_unary(
                '/sight.x.service.SightService/FetchOptimalAction',
                request_serializer=sight__service_dot_proto_dot_service__pb2.FetchOptimalActionRequest.SerializeToString,
                response_deserializer=sight__service_dot_proto_dot_service__pb2.FetchOptimalActionResponse.FromString,
                )
        self.ProposeAction = channel.unary_unary(
                '/sight.x.service.SightService/ProposeAction',
                request_serializer=sight__service_dot_proto_dot_service__pb2.ProposeActionRequest.SerializeToString,
                response_deserializer=sight__service_dot_proto_dot_service__pb2.ProposeActionResponse.FromString,
                )
        self.FinalizeEpisode = channel.unary_unary(
                '/sight.x.service.SightService/FinalizeEpisode',
                request_serializer=sight__service_dot_proto_dot_service__pb2.FinalizeEpisodeRequest.SerializeToString,
                response_deserializer=sight__service_dot_proto_dot_service__pb2.FinalizeEpisodeResponse.FromString,
                )


class SightServiceServicer(object):
    """This API manages Sight logs, their creation and access to them.
    """

    def Test(self, request, context):
        """A test request to validate that the service is up.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """rpc PrintInsertionTime(TestRequest) returns (TestResponse) {}
        Creates a new Sight log.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Launch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DecisionPoint(self, request, context):
        """rpc GetWeights(GetWeightsRequest) returns (GetWeightsResponse) {}
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Tell(self, request, context):
        """rpc DecisionOutcome(DecisionOutcomeRequest)
        returns (DecisionOutcomeResponse) {}
        rpc CopyDataToReplayServer(CopyDataToReplayServerRequest) returns (CopyDataToReplayServerResponse) {}
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Listen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CurrentStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchOptimalAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProposeAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinalizeEpisode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SightServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Test': grpc.unary_unary_rpc_method_handler(
                    servicer.Test,
                    request_deserializer=sight__service_dot_proto_dot_service__pb2.TestRequest.FromString,
                    response_serializer=sight__service_dot_proto_dot_service__pb2.TestResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=sight__service_dot_proto_dot_service__pb2.CreateRequest.FromString,
                    response_serializer=sight__service_dot_proto_dot_service__pb2.CreateResponse.SerializeToString,
            ),
            'Launch': grpc.unary_unary_rpc_method_handler(
                    servicer.Launch,
                    request_deserializer=sight__service_dot_proto_dot_service__pb2.LaunchRequest.FromString,
                    response_serializer=sight__service_dot_proto_dot_service__pb2.LaunchResponse.SerializeToString,
            ),
            'DecisionPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.DecisionPoint,
                    request_deserializer=sight__service_dot_proto_dot_service__pb2.DecisionPointRequest.FromString,
                    response_serializer=sight__service_dot_proto_dot_service__pb2.DecisionPointResponse.SerializeToString,
            ),
            'Tell': grpc.unary_unary_rpc_method_handler(
                    servicer.Tell,
                    request_deserializer=sight__service_dot_proto_dot_service__pb2.TellRequest.FromString,
                    response_serializer=sight__service_dot_proto_dot_service__pb2.TellResponse.SerializeToString,
            ),
            'Listen': grpc.unary_unary_rpc_method_handler(
                    servicer.Listen,
                    request_deserializer=sight__service_dot_proto_dot_service__pb2.ListenRequest.FromString,
                    response_serializer=sight__service_dot_proto_dot_service__pb2.ListenResponse.SerializeToString,
            ),
            'CurrentStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.CurrentStatus,
                    request_deserializer=sight__service_dot_proto_dot_service__pb2.CurrentStatusRequest.FromString,
                    response_serializer=sight__service_dot_proto_dot_service__pb2.CurrentStatusResponse.SerializeToString,
            ),
            'FetchOptimalAction': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchOptimalAction,
                    request_deserializer=sight__service_dot_proto_dot_service__pb2.FetchOptimalActionRequest.FromString,
                    response_serializer=sight__service_dot_proto_dot_service__pb2.FetchOptimalActionResponse.SerializeToString,
            ),
            'ProposeAction': grpc.unary_unary_rpc_method_handler(
                    servicer.ProposeAction,
                    request_deserializer=sight__service_dot_proto_dot_service__pb2.ProposeActionRequest.FromString,
                    response_serializer=sight__service_dot_proto_dot_service__pb2.ProposeActionResponse.SerializeToString,
            ),
            'FinalizeEpisode': grpc.unary_unary_rpc_method_handler(
                    servicer.FinalizeEpisode,
                    request_deserializer=sight__service_dot_proto_dot_service__pb2.FinalizeEpisodeRequest.FromString,
                    response_serializer=sight__service_dot_proto_dot_service__pb2.FinalizeEpisodeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sight.x.service.SightService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SightService(object):
    """This API manages Sight logs, their creation and access to them.
    """

    @staticmethod
    def Test(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sight.x.service.SightService/Test',
            sight__service_dot_proto_dot_service__pb2.TestRequest.SerializeToString,
            sight__service_dot_proto_dot_service__pb2.TestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sight.x.service.SightService/Create',
            sight__service_dot_proto_dot_service__pb2.CreateRequest.SerializeToString,
            sight__service_dot_proto_dot_service__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Launch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sight.x.service.SightService/Launch',
            sight__service_dot_proto_dot_service__pb2.LaunchRequest.SerializeToString,
            sight__service_dot_proto_dot_service__pb2.LaunchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DecisionPoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sight.x.service.SightService/DecisionPoint',
            sight__service_dot_proto_dot_service__pb2.DecisionPointRequest.SerializeToString,
            sight__service_dot_proto_dot_service__pb2.DecisionPointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Tell(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sight.x.service.SightService/Tell',
            sight__service_dot_proto_dot_service__pb2.TellRequest.SerializeToString,
            sight__service_dot_proto_dot_service__pb2.TellResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Listen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sight.x.service.SightService/Listen',
            sight__service_dot_proto_dot_service__pb2.ListenRequest.SerializeToString,
            sight__service_dot_proto_dot_service__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CurrentStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sight.x.service.SightService/CurrentStatus',
            sight__service_dot_proto_dot_service__pb2.CurrentStatusRequest.SerializeToString,
            sight__service_dot_proto_dot_service__pb2.CurrentStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchOptimalAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sight.x.service.SightService/FetchOptimalAction',
            sight__service_dot_proto_dot_service__pb2.FetchOptimalActionRequest.SerializeToString,
            sight__service_dot_proto_dot_service__pb2.FetchOptimalActionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProposeAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sight.x.service.SightService/ProposeAction',
            sight__service_dot_proto_dot_service__pb2.ProposeActionRequest.SerializeToString,
            sight__service_dot_proto_dot_service__pb2.ProposeActionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FinalizeEpisode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sight.x.service.SightService/FinalizeEpisode',
            sight__service_dot_proto_dot_service__pb2.FinalizeEpisodeRequest.SerializeToString,
            sight__service_dot_proto_dot_service__pb2.FinalizeEpisodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
