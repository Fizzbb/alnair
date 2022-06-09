# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import databus_pb2 as databus__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ConnectionStub(object):
    """set up connection between user and GM
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Connect = channel.unary_unary(
                '/databus.Connection/Connect',
                request_serializer=databus__pb2.ConnectRequest.SerializeToString,
                response_deserializer=databus__pb2.ConnectResponse.FromString,
                )


class ConnectionServicer(object):
    """set up connection between user and GM
    """

    def Connect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConnectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Connect': grpc.unary_unary_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=databus__pb2.ConnectRequest.FromString,
                    response_serializer=databus__pb2.ConnectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'databus.Connection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Connection(object):
    """set up connection between user and GM
    """

    @staticmethod
    def Connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/databus.Connection/Connect',
            databus__pb2.ConnectRequest.SerializeToString,
            databus__pb2.ConnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RegistrationStub(object):
    """register a DLT Client (DLTC) to the Global Manager (GM)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/databus.Registration/Register',
                request_serializer=databus__pb2.RegisterRequest.SerializeToString,
                response_deserializer=databus__pb2.RegisterResponse.FromString,
                )
        self.Deresgister = channel.unary_unary(
                '/databus.Registration/Deresgister',
                request_serializer=databus__pb2.DeregisterRequest.SerializeToString,
                response_deserializer=databus__pb2.DeregisterResponse.FromString,
                )


class RegistrationServicer(object):
    """register a DLT Client (DLTC) to the Global Manager (GM)
    """

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deresgister(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegistrationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=databus__pb2.RegisterRequest.FromString,
                    response_serializer=databus__pb2.RegisterResponse.SerializeToString,
            ),
            'Deresgister': grpc.unary_unary_rpc_method_handler(
                    servicer.Deresgister,
                    request_deserializer=databus__pb2.DeregisterRequest.FromString,
                    response_serializer=databus__pb2.DeregisterResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'databus.Registration', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Registration(object):
    """register a DLT Client (DLTC) to the Global Manager (GM)
    """

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/databus.Registration/Register',
            databus__pb2.RegisterRequest.SerializeToString,
            databus__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deresgister(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/databus.Registration/Deresgister',
            databus__pb2.DeregisterRequest.SerializeToString,
            databus__pb2.DeregisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class UpdatePolicyStub(object):
    """When key is not available, CC request GM to update policy
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Update = channel.unary_unary(
                '/databus.UpdatePolicy/Update',
                request_serializer=databus__pb2.UpdatePolicyRequest.SerializeToString,
                response_deserializer=databus__pb2.UpdatePolicyResponse.FromString,
                )


class UpdatePolicyServicer(object):
    """When key is not available, CC request GM to update policy
    """

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UpdatePolicyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=databus__pb2.UpdatePolicyRequest.FromString,
                    response_serializer=databus__pb2.UpdatePolicyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'databus.UpdatePolicy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UpdatePolicy(object):
    """When key is not available, CC request GM to update policy
    """

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/databus.UpdatePolicy/Update',
            databus__pb2.UpdatePolicyRequest.SerializeToString,
            databus__pb2.UpdatePolicyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class HeartbeatStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HB = channel.unary_unary(
                '/databus.Heartbeat/HB',
                request_serializer=databus__pb2.HearbeatMessage.SerializeToString,
                response_deserializer=databus__pb2.HearbeatMessage.FromString,
                )


class HeartbeatServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HB(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HeartbeatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HB': grpc.unary_unary_rpc_method_handler(
                    servicer.HB,
                    request_deserializer=databus__pb2.HearbeatMessage.FromString,
                    response_serializer=databus__pb2.HearbeatMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'databus.Heartbeat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Heartbeat(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HB(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/databus.Heartbeat/HB',
            databus__pb2.HearbeatMessage.SerializeToString,
            databus__pb2.HearbeatMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class LoggerStub(object):
    """CC periodically sends log messages tO GM
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.call = channel.stream_unary(
                '/databus.Logger/call',
                request_serializer=databus__pb2.LogItem.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class LoggerServicer(object):
    """CC periodically sends log messages tO GM
    """

    def call(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LoggerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'call': grpc.stream_unary_rpc_method_handler(
                    servicer.call,
                    request_deserializer=databus__pb2.LogItem.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'databus.Logger', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Logger(object):
    """CC periodically sends log messages tO GM
    """

    @staticmethod
    def call(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/databus.Logger/call',
            databus__pb2.LogItem.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
