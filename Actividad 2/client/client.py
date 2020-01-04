#!/usr/bin/env python
import pika
import sys
import time
import threading
import random

def hablar():

	while(True):

		connection = pika.BlockingConnection(
		    pika.ConnectionParameters(host='localhost'))
		channel = connection.channel()

		channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

		print("Escriba mensaje:")
		message = input()

		receiver = ""
		print("Destinatario:")
		receiver = input()

		message = username+"-"+message+"-"+receiver
		print(" [x] Sent to server: %r" % (message))

		channel.basic_publish(
		    exchange='direct_logs', routing_key="server-chat", body=message)
		connection.close()

def escuchar():
	connection = pika.BlockingConnection(
	    pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

	result = channel.queue_declare(queue='', exclusive=True)
	queue_name = result.method.queue

	channel.queue_bind(
	        exchange='direct_logs', queue=queue_name,  routing_key=username)

	print(' [*] Waiting for messages...')


	def callback(ch, method, properties, body):
		username,message = tuple(body.decode("utf-8").split("-"))
		print(" [x] Message received from %r:%r" % (username, message))


	channel.basic_consume(
	    queue=queue_name, on_message_callback=callback, auto_ack=True)

	channel.start_consuming()

def crearUsuario():

	global username
	print ("Escriba nombre de usuario (sin guion y sin repetir otro username):")
	username = input()


	connection = pika.BlockingConnection(
	pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

	message = username
	channel.basic_publish(
	    exchange='direct_logs', routing_key="server-newUsername", body=message)
	print(" [x] Username enviado")
	connection.close()

	#una vez enviada la solicitud el usuario quedarà esperando una respuesta

	connection = pika.BlockingConnection(
	    pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

	result = channel.queue_declare(queue='', exclusive=True)
	queue_name = result.method.queue

	channel.queue_bind(
	        exchange='direct_logs', queue=queue_name,  routing_key=username+"-accepted")

	print(' [*] Waiting confirmation...')


	def callback(ch, method, properties, body):
		if body.decode("utf-8") == "ok":
			connection.close()
			print(" [x] Confirmation username received")
		else:
			crearUsuario()


	channel.basic_consume(
	    queue=queue_name, on_message_callback=callback, auto_ack=True)

	channel.start_consuming()

#espera un poco para que rabbitqm este operando
print("Bienvenido, inicializando...")
time.sleep(17)



username = ""
crearUsuario()

print ("Usuario creado como",username)


thread_escuchar = threading.Thread(target=escuchar)
thread_hablar = threading.Thread(target=hablar)
thread_escuchar.start()
thread_hablar.start()
