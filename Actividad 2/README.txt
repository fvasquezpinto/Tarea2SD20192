1 Esta actividad se ejecuta con

	1 sudo docker-compose build

	2 sudo docker-compose up

En caso de que salga un error de fallo de conexión puede deberse a que server.py o client1.py o client2.py inicializó antes de que RabbitQM estuviera totalmente operativa. Volver a intentarlo. Los clientes enviaràn mensajes con un numero aleatorio cada 10 segundos.


2 Para agregar un nuevo cliente a la arquitectura

	2.1. Una vez ejecutada la parte 1, en un nuevo terminal ir a la carpeta client de la actividad 2 (PATH: /Tarea2SD20192/Actividad\ 2/client) y ejecutar el comando:  sudo docker image build -t client_n .
	Importante: en el comando anterior hay un punto (.) al final, no ignorar.
	2.2. Ejecutar el comando: sudo docker container run  -v absolute_path_a_la_carpeta_client_de_la_actividad_2:/client/ --network host -i -t client_n
    

	Ejemplo: en el computador de Francisco(Mac), se ejecutó con el siguiente absolute path a la carpeta cliente de la actividad 2:
    	sudo docker container run  -v /Users/francisco/Desktop/git/Tarea2SD20192/Actividad\ 2/client:/client/ --network host -i -t client_n
	Mientras que en el computador de Gabriel(Ubuntu), se ejecutò con el siguiente absolute path:
	sudo docker container run  -v /home/gabriel/Escritorio/Tarea2SD20192/Actividad\ 2/client3/:/client3/ --network host -i -t client_3

