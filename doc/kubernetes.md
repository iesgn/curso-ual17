# Kubernetes

Es un proyecto open source de Google para la gestión de aplicaciones en contenedores, en especial los contenedores Docker, permitiendo programar el despliegue, escalado, monitorización de los contenedores, etc.

## Arquitectura

Un clúster de Kubernetes está formado por nodos o minions (kubelet) y por los componentes del Master (APIs, scheduler, etc) encima de una solución de almacenamiento distribuido.

imagen

## Kubernetes Master

El servidor master va a controlar el clúster. Es el punto dónde se otorga a los servicios de clúster información de todos los nodos, y corre los siguientes servicios:

* etcd: es una base de datos altamente disponible que almacena
claves-valor en el que Kubernetes almacena información (configuración y metadatos) acerca del estado del cluster.
* Scheduler (Kube-scheduler): se encarga de distribuir los pods entre los nodos, asigna los pods a los nodos. También es el responsable de monitorizar la utilización de recursos de cada host para asegurar que los pods no sobrepasen los recursos disponibles.
* API Server (kube-apiserver): Provee la API que controla la orquestación de Kubernetes El apiserver expone una interfaz REST.
* Controller manager: es un servicio usado para manejar el proceso de replicación definido en las tareas de replicación. 

## Kubernetes Node

En el nodo se ejecutan todos los componentes y servicios necesarios para correr aplicaciones y balancear el tráfico entre servicios (endpoints). Posee los siguientes servicios:

* Docker   o   rkt: son los motores de contenedores que funcionan en cada nodo descargando y corriendo las imágenes docker. Son controlados a través de sus APIs por Kubelet.
Kubelet: gestiona los pods y sus contenedores, sus imágenes, sus volúmenes, etc. Cada nodo corre un Kubelet, que es el responsable del registro de cada nodo y de la gestión de los pods.
* cAdvisor: es un agente de uso de los recursos y análisis que descubre todos los contenedores en la máquina y recoge
información sobre CPU, memoria, sistema de ficheros y estadísticas de uso de la red. 
* Flannel: provee redes y conectividad para los nodos y contenedores en el clúster. 
* Proxy (Kube-proxy): provee servicios de proxy de red. Cada nodo también ejecuta un proxy y un balanceador de carga. 

## Otros conceptos

* PODs (dockers): son la unidad más pequeña desplegable que puede ser creada, programada y manejada por Kubernetes. Son un grupo de contenedores Dockers, de aplicaciones que comparten volúmenes y red. 
* Replication   Controller: se asegura de que el número especificado de réplicas del pod estén ejecutándose y funcionando en todo momento. 
Clúster: Conjunto de máquinas físicas o virtuales y otros recursos (almacenamiento, red, etc.) utilizados por Kubernetes dónde pods son desplegados, gestionados y replicados. 
* Service: es una abstracción (un nombre único) que define un conjunto de pods y la lógica para acceder a los mismos. Los servicios ofrecen la capacidad para buscar y distribuir el tráfico proporcionando un nombre y dirección o puerto persistente para los pods con un conjunto común de labels.
Labels: son pares clave/valor usados para agrupar, organizar y seleccionar un grupo de objetos tales como Pods. Son fundamentales para que los services y los replications controllers obtengan la lista de los servidores a donde el tráfico debe pasar.