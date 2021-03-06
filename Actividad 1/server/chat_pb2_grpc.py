# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import chat_pb2 as chat__pb2
import id_mapper_pb2 as id__mapper__pb2


class ChatStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.send_receive = channel.unary_unary(
        '/Chat/send_receive',
        request_serializer=chat__pb2.ChatRequest.SerializeToString,
        response_deserializer=chat__pb2.ChatReply.FromString,
        )
    self.Get_client_msgs_list = channel.unary_unary(
        '/Chat/Get_client_msgs_list',
        request_serializer=id__mapper__pb2.Number.SerializeToString,
        response_deserializer=chat__pb2.StringList.FromString,
        )


class ChatServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def send_receive(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get_client_msgs_list(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'send_receive': grpc.unary_unary_rpc_method_handler(
          servicer.send_receive,
          request_deserializer=chat__pb2.ChatRequest.FromString,
          response_serializer=chat__pb2.ChatReply.SerializeToString,
      ),
      'Get_client_msgs_list': grpc.unary_unary_rpc_method_handler(
          servicer.Get_client_msgs_list,
          request_deserializer=id__mapper__pb2.Number.FromString,
          response_serializer=chat__pb2.StringList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Chat', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
