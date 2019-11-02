Levantar la Arquitectura

1. Encender Docker Desktop; esperar hasta que indique "Docker Desktop is running"
2. Abrir una terminal en la carpeta Actividad 1 (Tarea2SD20192/Actividad\ 1):
	2.1 Ejecutar el comando:
		docker-compose build
		Esperar hasta que termine de construir

	2.2 Ejecutar el comando:
		docker-compose up

	Nota: no se puede ingresar mensajes por línea de comandos a los clientes levantados con docker-compose up, pues al levantarlos con dicho comando
	Docker no permite ingresar inputs. Sin embargo, la línea de comandos donde se hizo el docker-compose up sí mostrará los mensajes que reciban
	los clientes 1 y 2 (levantados con dicho docker-compose up).



Agregar un nuevo cliente a la arquitectura

1. Abrir una terminal en la carpeta client de la actividad 1 (PATH: /Tarea2SD20192/Actividad\ 1/client) y ejecutar el comando:  docker image build -t client_n .
	Importante: al final del comando anterior hay un punto (.), no ignorar.
2. Ejecutar el comando: docker container run  -v absolute_path_a_la_carpeta_client_de_la_actividad_1:/client/ --network host -i -t client_n
    Ejemplo: en el computador de Francisco, se ejecutó con el siguiente absolute path a la carpeta cliente de la actividad 1:
    	docker container run  -v /Users/francisco/Desktop/git/Tarea2SD20192/Actividad\ 1/client:/client/ --network host -i -t client_n



Usar línea de comandos para interactuar con el sistema como cliente

Importante: A cada cliente es asignado un ID (ejemplo: 1) que será usado para identificar a cada cliente en el envío y recepción de mensajes.

1.	En una terminal en que se haya agregado un nuevo cliente se ofrecerán las siguientes opciones:

		Ingrese la opcion que desea ejecutar: 
		1: Enviar un mensaje (para enviarlo directamente ingrese destinatario,mensaje)
		2: Obtener listado completo de clientes
		3: Obtener listado de los mensajes que he enviado

	A continuación se debe ingresar, en la línea de comandos, el número de la opción deseada.

	Ejemplo si se elije 1:

		La línea de comandos indicará:

			Ingrese el destinatario y el mensaje en el formato:
			ID_destinatario,mensaje

		Una entrada válida sería ingresar entonces:

			1,hola

		Tras ello se informará que el mensaje se ha enviado; el mensaje aparecerá en la terminal donde está corriendo el cliente 1 (lo recibe).
		Vale decir, que en el caso anterior el ID del cliente al que se le envía el mensaje es 1. Y el mensaje que se envía es "hola"

	Ejemplo si elije 2:

		Pidiendo la lista completa de clientes...
		Server >>>  [1, 2, 3, 4]


	Ejemplo si elije 3, la línea de comandos mostrará:

		Pidiendo todos los mensajes que he enviado...
		Server >>>  ['Msg: holaa, To: 1, At: Saturday, November 02, 2019 02:57:41']

2. Para ver los mensajes que ha recibido un cliente, basta con observar la terminal donde está corriendo dicho cliente.

