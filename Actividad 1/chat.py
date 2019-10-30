# Los mensajes tienen la forma: msg = "id;timestamptexto_mensaje", donde id = "idEmisor_timestamp"

msgs_queues = {}

f = open("log.txt","a+")
f.write("Emisor\t\tFecha y hora\t\tMensaje\n")
f.write("-----------------------------------------------\n")
f.close()

def chat(src = "", dst = "", msg = ""):

	global msgs_queues
	global f

	# Caso de recepcion de mensaje en el servidor
	if src != "" and dst != "" and msg != "":

		if dst not in msgs_queues.keys():

			msgs_queues[dst] = []

		msgs_queues[dst].append(msg)
		f = open("log.txt","a+")
		f.write(src + "\t\t" + msg.split(";")[2] + "\t\t" + msg.split(";")[1] + "\n")
		f.close()

		return "Message received"

	# Caso de envio de un mensaje desde el servidor; el src en este caso corresponde al cliente que pide sus mensajes
	elif src != "" and dst == "" and msg == "":

		income_msgs = ""

		if src in msgs_queues.keys():

			for msg in msgs_queues[src]:

				income_msgs += "Msg: " + msg.split(";")[1] + ", From: " + msg.split(";")[0].split("_")[0] + ", At: " + msg.split(";")[2] + ";"

			msgs_queues[src] = []

		return income_msgs






