import pika
import sys
import datetime
import threading
import time

def recibirYEnviarMensajes():

	#recibir mensajes
	connection = pika.BlockingConnection(
	    pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	
	channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

	result = channel.queue_declare(queue='', exclusive=True)
	queue_name = result.method.queue

	channel.queue_bind(
	        exchange='direct_logs', queue=queue_name,  routing_key="server-chat")

	print(' [*] Esperando mensajes')

	def callback(ch, method, properties, body):
		sender,message,receiver = tuple(body.decode("utf-8").split("-"))
		print(" [x] Message received from %r to %r: %r" % (sender,receiver,message))
		file = open("log.txt","a")
		file.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + "\t\t" + sender + "\t\t"+ receiver + "\t\t" + message + "\n")
		file.close()

		connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
		channel = connection.channel()

		channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
		
		channel.basic_publish(exchange='direct_logs', routing_key=receiver, body=sender+"-"+message)
		print(" [x] Sent message from %r to %r: %r" % (sender, receiver, message))
		connection.close()



	channel.basic_consume(
	    queue=queue_name, on_message_callback=callback, auto_ack=True)

	channel.start_consuming()


def conectarUsers():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

	result = channel.queue_declare(queue='', exclusive=True)
	queue_name = result.method.queue

	channel.queue_bind(
	        exchange='direct_logs', queue=queue_name,  routing_key="server-newUsername")

	print(' [*] Esperando a que usuarios se conecten. ')


	def callback(ch, method, properties, body):
		list_users.append(len(list_users))
		file = open("list_users.txt","a")
		newUser = body.decode("utf-8").strip()
		file.write(str(len(list_users)) + "\t\t" +newUser+"\n")
		file.close()

		#Una vez registrado el usuario se envia una respuesta al cliente

		time.sleep(2)

		connection2 = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
		channel = connection2.channel()

		channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
		
		channel.basic_publish(exchange='direct_logs', routing_key=newUser+"-accepted", body="ok")

		print(" [x] Sent message 'ok' to %r" % (newUser))

		time.sleep(2)

		print(" [x] user created: %r" % (newUser))

		connection2.close()


	channel.basic_consume(
	    queue=queue_name, on_message_callback=callback, auto_ack=True)

	channel.start_consuming()

list_users = list()
file = open("log.txt","w")
file.write("Fecha y hora\t\tEmisor\t\tReceptor\t\tMensaje\n")
file.write("---------------------------------------------------------------\n")
file.close()
file = open("list_users.txt","w")
file.write("ID\t\tUsername")
file.write("---------------------------------------------------------------\n")
file.close()
time.sleep(17)
thread_conectarUsers = threading.Thread(target=conectarUsers)
thread_recibirYEnviarMensajes = threading.Thread(target=recibirYEnviarMensajes)
thread_conectarUsers.start()
thread_recibirYEnviarMensajes.start()
