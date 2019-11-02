Agregar un nuevo cliente a la arquitectura

1. Ir a la carpeta client de la actividad 1 (PATH: /Tarea2SD20192/Actividad\ 1/client) y ejecutar el comando:  docker image build -t client_n .
	Importante: en el comando anterior hay un punto (.) al final, no ignorar.
2. Ejecutar el comando: docker container run  -v absolute_path_a_la_carpeta_client_de_la_actividad_1:/client/ --network host -i -t client_n
    Ejemplo: en el computador de Francisco, se ejecutó con el siguiente absolute path a la carpeta cliente de la actividad 1:
    	docker container run  -v /Users/francisco/Desktop/git/Tarea2SD20192/Actividad\ 1/client:/client/ --network host -i -t client_n