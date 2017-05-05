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
