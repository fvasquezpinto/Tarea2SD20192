import grpc
import time
from datetime import datetime, timedelta
import threading
import re

import id_mapper_pb2
import id_mapper_pb2_grpc

import chat_pb2
import chat_pb2_grpc


class ReceiveMessages(threading.Thread):
	def run(self):

		global flag_thread_stop

		while True:

			if flag_thread_stop == 1:
				break

			# Recibir mensajes
			#print("Pidiendo mis mensajes...")
			chat_request = chat_pb2.ChatRequest(src = str(my_id), dst = "", msg = "")
			response = stub_chat.send_receive(chat_request)
			if str(response.message) != '':
				print("Ha(n) llegado mensaje(s):\n")

				for msg_to_client in str(response.message).split(";/;;/;///;"):

					print(msg_to_client)

				print("")

				#print("Server >>> ", str(response.message))
				#print("")
			time.sleep(1)
		

current_msg_number = 0

flag_thread_stop = 0

channel = grpc.insecure_channel('localhost:5000')

stub_id_mapper = id_mapper_pb2_grpc.ID_mapperStub(channel)
stub_chat = chat_pb2_grpc.ChatStub(channel)

# Adquirir un ID para operar en la arquitectura
print("Pidiendo al server un ID...")
response = stub_id_mapper.ID_map(id_mapper_pb2.Empty())
#print("Server >>> ", response.value)
#print("")
my_id = response.value

print("Mi ID es: ", my_id)

thread = ReceiveMessages()
thread.start()


try:
	while True:

		user_option = input("Ingrese la opcion que desea ejecutar: \n1: Enviar un mensaje (para enviarlo directamente ingrese ID_destinatario,mensaje)\n2: Obtener listado completo de clientes\n3: Obtener listado de los mensajes que he enviado\n")
		print("")
		if user_option == '1':

			user_message = input("Ingrese el destinatario y el mensaje en el formato:\nID_destinatario,mensaje\n")

			# Enviar un mensaje
			# Los mensajes tienen la siguiente estructura: idClient_MsgNumberByClient;MsgBody;Timestamp
			# Importante: datetime tiene el formato "yyyy-mm-dd time", por lo que asi quedara el timestamp
			# Importante2: se asume que no es ilegal que se envie mensaje a si mismo
			user_message_splitted = user_message.split(',')
			try:
				user_message_splitted[1]
			except:
				print("IMPORTANTE: Debe ingresar el destinatario y el mensaje en el formato:\nID_destinatario,mensaje\nmensaje debe ser alfanumerico\n")
				continue

			if len(user_message_splitted[0]) > 0 and len(user_message_splitted[1]) > 0:

				target = user_message_splitted[0]
				message = user_message_splitted[1]

				print("Pidiendo al server el envio de un mensaje...")
				msg_to_send = str(my_id) + "_" + str(current_msg_number) + ";" + message + ";" + str((datetime.now() + timedelta(hours=-3)).strftime("%A, %B %d, %Y %H:%M:%S"))
				chat_request = chat_pb2.ChatRequest(src = str(my_id), dst = target, msg = msg_to_send)
				current_msg_number += 1
				response = stub_chat.send_receive(chat_request)
				print("Servidor dice: ", str(response.message))
				print("")

			else:
				print("IMPORTANTE: Debe ingresar el destinatario y el mensaje en el formato:\nID_destinatario,mensaje\nmensaje debe ser alfanumerico\n")
				continue


		elif user_option == '2':

			# Pedir lista de clientes
			print("Pidiendo la lista completa de clientes...")
			response = stub_id_mapper.Get_clients_list(id_mapper_pb2.Empty())
			print("Lista de clientes: ", response.clients_list)
			print("")

		elif user_option == '3':

			# Pedir todos los mensajes que ha enviado este cliente
			print("Pidiendo todos los mensajes que he enviado...")
			print("")
			client_msg_request = id_mapper_pb2.Number(value = my_id)
			response = stub_chat.Get_client_msgs_list(client_msg_request)
			for client_msg in response.client_msgs_list:
				print(client_msg)
			print("")


			#time.sleep(86400)

		else:

			if re.match("^[0-9]+,[A-Za-z0-9 ]+$", user_option):

				# Enviar un mensaje
				# Los mensajes tienen la siguiente estructura: idClient_MsgNumberByClient;MsgBody;Timestamp
				# Importante: datetime tiene el formato "yyyy-mm-dd time", por lo que asi quedara el timestamp
				user_message_splitted = user_option.split(',')
				try:
					user_message_splitted[1]
				except:
					print("IMPORTANTE: Debe ingresar el destinatario y el mensaje en el formato:\nID_destinatario,mensaje\nmensaje debe ser alfanumerico\n")
					continue

				if len(user_message_splitted[0]) > 0 and len(user_message_splitted[1]) > 0:

					target = user_message_splitted[0]
					message = user_message_splitted[1]

					print("Pidiendo al server el envio de un mensaje...")
					msg_to_send = str(my_id) + "_" + str(current_msg_number) + ";" + message + ";" + str((datetime.now() + timedelta(hours=-3)).strftime("%A, %B %d, %Y %H:%M:%S"))
					chat_request = chat_pb2.ChatRequest(src = str(my_id), dst = target, msg = msg_to_send)
					current_msg_number += 1
					response = stub_chat.send_receive(chat_request)
					print("Servidor dice: ", str(response.message))
					print("")

				else:
					print("IMPORTANTE: Debe ingresar el destinatario y el mensaje en el formato:\nID_destinatario,mensaje\nmensaje debe ser alfanumerico\n")
					continue



except KeyboardInterrupt:
    flag_thread_stop = 1