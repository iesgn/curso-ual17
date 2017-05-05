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

## Creación de deployments

Es más usual crear el deployment que será el responsable de crear los pods indicados. Los deployments es un nuevo mecanismo para controlar la ejecución de pods, anteriormente se usaba un Replication Controller. 

Para definir un deployment creamos un fichero yaml, por ejemplo nginx-deploy.yaml:

	apiVersion: apps/v1beta1
	kind: Deployment
	metadata:
	    name: my-nginx
	spec:
	    replicas: 1
	    template:
	      metadata:
	        labels:
	          app: nginx
	      spec:
	        containers:
	        - name: nginx
	          image: nginx
	          ports:
	          - containerPort: 80

Y para crear el deployment ejecutamos:

	$ kubectl create -f nginx-deploy.yaml
	deployment "my-nginx" created

	$ kubectl get deploy
	NAME       DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
	my-nginx   1         1         1            1           16s

	$ kubectl get pods
	NAME                        READY     STATUS    RESTARTS   AGE
	my-nginx-2122188915-hs8mt   1/1       Running   0          36s

Además el deployment crea un recurso ReplicaSet, que asegura que un número especificado de "réplicas" de pod estén en ejecución en un momento dado. Sin embargo, un deployment es un concepto de nivel superior que administra ReplicaSets y PODS. Por lo tanto, es recomendable usar Deployments en lugar de utilizar directamente ReplicaSets.

	$ kubectl get rs
	NAME                  DESIRED   CURRENT   READY     AGE
	my-nginx-2122188915   1         1         1         50s




