# El concepto

"Las múltiples capas de software que vamos interponiendo entre el hardware y las aplicaciones precisan que las gestionemos automáticamente"


## ¿Qué capas?

- Virtualización
- Contenedores
- SDN
- SDS
- Infraestructura como servicio: IaaS
- Container Orchestration Engine: COE 

## IaaS y COE

La IaaS está pensada para gestionar todos los recursos de
infraestructura de modo que el usuario los pueda gestionar fácilmente
a través de una API bien definida. 

La principal ventaja del uso de IaaS es que se pueden modificar de
forma rápida todos los recursos, una propiedad que se denomina
*elasticidad*.

El software de IaaS que veremos en este curso es OpenStack, un
software que empieza a madurar y estabilizarse tras años de desarrollo
desbocado. OpenStack es capaz de gestionar de forma muy eficiente la
capa de virtualización de máquinas, redes y almacenamiento. El encaje
de contenedores directamente en OpenStack no está tan claro y hay
múltiples opciones, que veremos más adelante.

Los COE son mucho más nuevos, tanto que ni si quiera este término está
comunmente aceptado, se utilizan también otros similares. Están
íntimamente relacionados al despliegue de una aplicación con una
arquitectura de *microservicios*, donde la base son múltiples
contenedores ejecutados en diferentes nodos que idealmente ejecutan
un solo proceso cada uno. Una gran ventaja de la arquitectura de
microservicios es que permite una mejor gestión de las versiones y
actualizaciones de las apliaciones y la utilización de prácticas
ágiles como CI/CD.

El campo de los COE está en estos momentos en plena ebullición en las
TI, apareciendo de forma continua todo tipo de aplicaciones que
intentan hacerse un hueco en un campo que está captando tanta
atención. Kubernetes, proyecto inicialmente gestionado por Google,
lleva la delantera, pero todavía queda mucho por ver y muchos
"cadáveres" se van a quedar por el camino.

Kubernetes es capaz de gestionar múltiples nodos (máquinas virtuales o
físicas) en los que se ejecutan contenedores sobre docker o rkt,
utilizando SDN y SDS de una forma limitada.

¿Dónde ubicaríamos OpenStack y Kubernetes en el famoso [ciclo de sobreexpectación](https://es.wikipedia.org/wiki/Ciclo_de_sobreexpectaci%C3%B3n)?

Tanto OpenStack como Kubernetes son grandes aplicaciones de software
que tienen algunas diferencias, pero con unas importantes
implicaciones comunes:

- Aplicaciones grandes con muchas opciones y difíciles de instalar
- Sometidas a un enorme desarrollo, no existe versión LTS lo que
  conlleva actualizaciones continuas
- Pueden convertirse en una pieza crítica en una organización, lo que
  exige monitorización, personal cualificado para gestionarlas y
  planificación de la respuesta a eventos.

## El sandwich

Para gestionar las aplicaciones de nuestra organización podemos
decantarnos por utilizar alguna de estas capas.

### Aplicaciones sobre OpenStack

Instalamos OpenStack sobre los servidores físicos y ejecutamos
aplicaciones que utilizan almacenamiento, redes y máquinas
gestionadas por OpenStack

*Sandwich de tres capas*

### Aplicaciones sobre Kubernetes

Instalamos Kubernetes sobre los servidores físicos y ejecutamos
aplicaciones que utilizan contenedores, almacenamiento y redes
gestionadas por Kubernetes y son accesibles a través de los
balanceadores de carga de kubernetes.
  
*Sandwich de tres capas*

### Aplicaciones sobre kubernetes que está sobre OpenStack

Podemos gestionar los nodos de kubernetes como instancias o servidores
físicos gestionados por OpenStack, así como las redes y el
almacenamiento que requieran, de forma que Kubernetes pasa a ser una
aplicación elástica que utiliza los recursos que requiere en cada
momento,

*Sandwich de cuatro capas*

### Aplicaciones sobre OpenStack que está sobre Kubernetes

OpenStack es una aplicación que puede encajar en una arquitectura de
microservicios y por tanto ejecutarla en Kubernetes aporta la
facilidad de instalación y actualización, algo muy importante en un
software complejo y en continua evolución.

*Sandwich de cuatro capas*

### Aplicaciones sobre Kubernetes que está sobre OpenStack que está sobre Kubernetes
	
Utilizamos dos COE diferentes, uno para la gestión del IaaS como una
aplicación con arquitectura de microservicios y otro para las
aplicaciones reales de nuestra organización.
	
*Sandwich completo especial de la casa*

A estas alturas te estás preguntando, ¿no estaba yo más agusto
ejecutando un servidor web sobre un servidor físico?

