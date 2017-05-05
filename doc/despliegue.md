# Despliegue de una aplicación en kubernetes

## Creación de PODS

Empezamos creados PODS por ínea de comandos:

	$ kubectl run webserver --image=nginx  --replicas=1 --port=80
	deployment "webserver" created

Donde se ha indicado la imagen, las replicas que se van a crear y el puerto de escucha.

Podemos obtener los pods que hemos creado, vemos que los pods se crean todos con el mismo nombre y un identificador único al final:

	$ kubectl get pods
	NAME                         READY     STATUS    RESTARTS   AGE
	webserver-2582186985-wltz1   1/1       Running   0          1m

Para obtener más información del POD:

	$ kubectl describe pods webserver-2582186985-wltz1

En realidad la instrucción que hemos usado anteriormente no crea un pod, crea un deployment:

	$ kubectl get deploy
	NAME        DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
	webserver   1         1         1            1           7m

Un deployment es un mecanismo que asegura que siempre tenemos el número de pods deseados y nos permite replicar los pods. Por lo tanto si intentamos borrar el pod, el deployment creará inmediatamente uno nuevo:

	$ kubectl delete pods webserver-2582186985-wltz1
	pod "webserver-2582186985-wltz1" deleted
	
	$ kubectl get pods
	NAME                         READY     STATUS              RESTARTS   AGE
	webserver-2582186985-r8tg8   0/1       ContainerCreating   0          5s

Por lo tanto para borrar el pod tenemos que borrar el deployment:

	$ kubectl delete deploy webserver
	deployment "webserver" deleted
	
	$ kubectl get pods
	NAME                         READY     STATUS        RESTARTS   AGE
	webserver-2582186985-r8tg8   0/1       Terminating   0          2m

	$ kubectl get pods
	No resources found.

## 
