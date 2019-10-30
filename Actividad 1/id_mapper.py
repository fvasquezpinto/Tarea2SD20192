count = 0
clients_list = []

def id_map():

	global count
	global clients_list

	count += 1
	clients_list.append(count)

	return count

def get_clients_list():

	return clients_list