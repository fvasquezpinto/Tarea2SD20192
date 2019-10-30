import grpc
import time
from datetime import datetime

import id_mapper_pb2
import id_mapper_pb2_grpc

import chat_pb2
import chat_pb2_grpc

current_msg_number = 0

channel = grpc.insecure_channel('localhost:5000')

stub_id_mapper = id_mapper_pb2_grpc.ID_mapperStub(channel)

# Adquirir un ID para operar en la arquitectura
print("Pidiendo al server un ID...")
response = stub_id_mapper.ID_map(id_mapper_pb2.Empty())
print("Server says: ", response.value)
print("")
my_id = response.value

stub_chat = chat_pb2_grpc.ChatStub(channel)

# Enviar un mensaje
# Los mensajes tienen la siguiente estructura: idClient_MsgNumberByClient;MsgBody;Timestamp
# Importante: datetime tiene el formato "yyyy-mm-dd time", por lo que asi quedara el timestamp
if my_id == 1:
	print("Pidiendo al server el envio de un mensaje...")
	msg_to_send = str(my_id) + "_" + str(current_msg_number) + ";" + "hola" + ";" + str(datetime.now())
	chat_request = chat_pb2.ChatRequest(src = str(my_id), dst = "2", msg = msg_to_send)
	current_msg_number += 1
	response = stub_chat.send_receive(chat_request)
	print("Server says: ", str(response.message))
	print("")

# Pedir lista de clientes
print("Pidiendo la lista completa de clientes...")
response = stub_id_mapper.Get_clients_list(id_mapper_pb2.Empty())
print("Server says: ", response.clients_list)
print("")

# Recibir mensajes
print("Pidiendo mis mensajes...")
chat_request = chat_pb2.ChatRequest(src = str(my_id), dst = "", msg = "")
response = stub_chat.send_receive(chat_request)
print("Server says: ", str(response.message))
print("")

# Pedir todos los mensajes que ha enviado este cliente
print("Pidiendo todos los mensajes que he enviado...")
client_msg_request = id_mapper_pb2.Number(value = my_id)
response = stub_chat.Get_client_msgs_list(client_msg_request)
print("Server says: ", response.client_msgs_list)
print("")


try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)