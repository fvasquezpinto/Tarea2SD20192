import grpc
from concurrent import futures
import time

import id_mapper_pb2
import id_mapper_pb2_grpc
import id_mapper

import chat_pb2
import chat_pb2_grpc
import chat



class ID_mapperServicer(id_mapper_pb2_grpc.ID_mapperServicer):

    def ID_map(self, request, context):
        response = id_mapper_pb2.Number()
        response.value = id_mapper.id_map()
        return response

    def Get_clients_list(self, request, context):
        response = id_mapper_pb2.IntList()
        response.clients_list.extend(id_mapper.get_clients_list())
        #for client_id in id_mapper.get_clients_list():

            #response.clients_list.append(client_id)

        return response

class ChatServicer(chat_pb2_grpc.ChatServicer):

    def send_receive(self, request, context):
        response = chat_pb2.ChatReply()
        response.message = chat.chat(str(request.src),str(request.dst),str(request.msg))
        return response

    def Get_client_msgs_list(self, request, context):
        response = chat_pb2.StringList()
        response.client_msgs_list.extend(chat.get_client_msgs_list(request.value))

        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

id_mapper_pb2_grpc.add_ID_mapperServicer_to_server(
        ID_mapperServicer(), server)

chat_pb2_grpc.add_ChatServicer_to_server(
        ChatServicer(), server)

print('Starting server. Listening on port 5000.')
server.add_insecure_port('[::]:5000')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)