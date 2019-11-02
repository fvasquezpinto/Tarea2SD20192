msgs_queues = {}

try:
	f = open("log.txt","r")
except:
	f = open("log.txt","w")

f.close()
f = open("log.txt","r")
lines = f.readlines()
flag_archivo_vacio = 0
if len(lines) == 0:
	flag_archivo_vacio = 1
f.close()

f = open("log.txt","a+")
if flag_archivo_vacio == 1:

	f.write("Emisor\t\tReceptor\t\tFecha y hora\t\tMensaje\n")
	f.write("---------------------------------------------------------------\n")

f.close()

def chat(src = "", dst = "", msg = ""):

	global msgs_queues
	global f

	# Caso de recepcion de mensaje en el servidor
	# Los mensajes tienen la siguiente estructura: idClient_MsgNumberByClient;MsgBody;Timestamp
	# Importante: datetime tiene el formato "yyyy-mm-dd time", por lo que asi quedara el timestamp
	if src != "" and dst != "" and msg != "":

		if dst not in msgs_queues.keys():

			msgs_queues[dst] = []

		msgs_queues[dst].append(msg)
		f = open("log.txt","a+")
		f.write(src  + "\t\t" + dst + "\t\t" + msg.split(";")[2] + "\t\t" + msg.split(";")[1])
		f.close()

		return "Message received"

	# Caso de envio de un mensaje desde el servidor; el src en este caso corresponde al cliente que pide sus mensajes
	# Los mensajes tienen la siguiente estructura: idClient_MsgNumberByClient;MsgBody;Timestamp
	# Importante: datetime tiene el formato "yyyy-mm-dd time", por lo que asi quedara el timestamp
	elif src != "" and dst == "" and msg == "":

		income_msgs = ""

		if src in msgs_queues.keys():

			for msg in msgs_queues[src]:

				income_msgs += "Msg: " + msg.split(";")[1] + ", From: " + msg.split(";")[0].split("_")[0] + ", At: " + msg.split(";")[2] + ";"

			msgs_queues[src] = []

		return income_msgs

def get_client_msgs_list(id_client):

	msgs_list = []
	f = open("log.txt","r")
	lines = f.readlines()
	f.close()

	contador = 0

	for line in lines:

		if contador < 2:
			contador += 1
			continue

		line_splitted = line.split("\t\t")
		if int(line_splitted[0]) == id_client:

			msgs_list.append("Msg: " + line_splitted[3] + ", To: " + line_splitted[1] + ", At: " + line_splitted[2])

	return msgs_list


