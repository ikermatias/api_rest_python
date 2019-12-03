# api_rest_python

1. En el nodo maestro inicializamos un cluster de Docker Swarm 'docker swaram init'

2. Docker swarm nos responderá con el Token a unirse al cluster (ver imagen 1)

3. Para más seguridad, revisamos que el nodo maestro tenga disponibilidad 'docker node ls' (ver imagen 2 )

4. Construimos nuestras imágenes docker que tendrán nuestros servicios (back y front) 'docker build -t api_backend ./backend' 'docker build -t api_frontend ./frontend'
 
5. En docker swarm, el despliegue de servicios se conoce como "stack" y se requiere de un docker-compose.yml para el despliegue del mismo. En nuestro docker-compose.yml tenemos la descripción de nuestro servicio de back y front. 'docker stack deploy -c docker-compose.yml stack_api' (ver imagen 3)

6. listamos los servicios del stack 'docker stack service stack_api" para ver los servicios que se han desplegado y validar su funcionamiento. (ver imagen 4) ... esperamos a que ambos estén en replicas 1/1

7. validamos su funcionamiento por el puerto 8081 :D !!

Finish 

