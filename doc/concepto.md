# El concepto

"Las múltiples capas de software que vamos interponiendo entre el hardware y las aplicaciones precisan que las gestionemos automáticamente"

Vamos a desarrollarlo ...

## Esquema clásico

- Almacenamiento NAS o SAN externo gestionado manualmente
- Gestión tradicional de redes ("control plane" y "data plane" en dispositivos hardware)
- Cada nodo tiene un sistema operativo instalado manualmente
- Las aplicaciones se despliegan manualmente sobre el sistema operativo del nodo o sobre una MV que corre en cada nodo
- En sistemas distribuidos podemos utilizar simultaneamente recursos de múltiples nodos, pero no es una solución general

### Tareas

- Monitorizar la aplicación, el sistema operativo y el sistema de virtualización
- Actualizar la aplicación
- Actualizar el sistema operativo

## Limitaciones

- Poco adecuado para aplicaciones con uso variable de recursos
- En general, hay una infrautilización de recursos
- Dependencia de proveedores de hardware en redes y almacenamiento
- Esquema estático y rígido

## Nuevos actores

- Arquitectura de microservicios. Contenedores
- SDN
- SDS
- IaaS
- 