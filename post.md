## Configuración post-instalación

### Creación de la red externa

La red externa es típicamente una red que proporciona conexión con el
exterior a las redes internas que posteriormente se crearán en
OpenStack.
Para crear la red externa accedemos al equipo donde hemos instalado
OpenStack y cargamos las credenciales de administrador, ya que la red
externa sólo la puede crear alguien con este rol:

    source admin_openrc.sh

Utilizando el cliente de línea de comandos de neutron que explicaremos
con detalle en temas posteriores creamos la red externa:

    neutron net-create ext-net --router:external \
    > --provider:physical_network external --provider:network_type flat
    Created a new network:
    +---------------------------+--------------------------------------+
    | Field                     | Value                                |
    +---------------------------+--------------------------------------+
    | admin_state_up            | True                                 |
    | id                        | 149a5666-72a7-4d7f-91e2-855548fb3cb3 |
    | mtu                       | 0                                    |
    | name                      | ext-net                              |
    | provider:network_type     | flat                                 |
    | provider:physical_network | external                             |
    | provider:segmentation_id  |                                      |
    | router:external           | True                                 |
    | shared                    | False                                |
    | status                    | ACTIVE                               |
    | subnets                   |                                      |
    | tenant_id                 | e87ac1a9b6344a5cbaf0011f738042c3     |
    +---------------------------+--------------------------------------+

El nombre "ext-net" es opcional, pero es el que habitualmente se
utiliza cuando sólo existe una red externa.
A continuación definimos una subred donde aparece la definición lógica
de la red y cuyos valores dependerán de la red privada o pública a la
que esté conectada. En este caso el equipo está conectado a la red
192.168.1.0/24 con la puerta de enlace 192.168.1.1 y vamos a utilizar
el segmento 192.168.1.150-192.168.1.160 para las direcciones IP
flotantes de las instancias que correran sobre OpenStack:

    neutron subnet-create ext-net 192.168.1.0/24 --name ext-subnet \
    > --allocation-pool start=192.168.1.150,end=192.168.1.160 \
    > --disable-dhcp --gateway 192.168.1.1
    +-------------------+----------------------------------------------+
    | Field             | Value                                        |
    +-------------------+----------------------------------------------+
    | allocation_pools  | {"start": "192.168.1.150", "end": "192.168...
    | cidr              | 192.168.1.0/24                               |
    | dns_nameservers   |                                              |
    | enable_dhcp       | False                                        |
    | gateway_ip        | 192.168.1.1                                  |
    | host_routes       |                                              |
    | id                | 20c498de-e130-4905-bc34-791e9202d5c5         |
    | ip_version        | 4                                            |
    | ipv6_address_mode |                                              |
    | ipv6_ra_mode      |                                              |
    | name              | ext-subnet                                   |
    | network_id        | 149a5666-72a7-4d7f-91e2-855548fb3cb3         |
    | subnetpool_id     |                                              |
    | tenant_id         | e87ac1a9b6344a5cbaf0011f738042c3             |
    +-------------------+----------------------------------------------+

### Creación de proyectos y usuarios
Inicialmente existen 3 proyectos:

    openstack project list
    +----------------------------------+---------+
    | ID                               | Name    |
    +----------------------------------+---------+
    | ad191e001ba54366960a4e73d2ff0c08 | service |
    | c83fa27062f442b1b4801c6af6a3c8d3 | demo    |
    | e87ac1a9b6344a5cbaf0011f738042c3 | admin   |
    +----------------------------------+---------+

El proyecto "admin" es obviamente utilizado por el administrador,
"service" es el utilizado por los componentes de OpenStack y los
usuarios de estos servicios (Nova, Glance, etc.) y "demo" es un
proyecto creado en esta instalación para hacer pruebas con un usuario
no privilegiado.
Para crear un nuevo proyecto basta con hacer:

    openstack project create demo2
    +-------------+----------------------------------+
    | Field       | Value                            |
    +-------------+----------------------------------+
    | description | None                             |
    | enabled     | True                             |
    | id          | 256c1358da4d41ea90ac2322e73e503f |
    | name        | demo2                            |
    +-------------+----------------------------------+

Y un usuario que luego pertenecerá a ese proyecto:

    openstack user create demo2
    +----------+----------------------------------+
    | Field    | Value                            |
    +----------+----------------------------------+
    | email    | None                             |
    | enabled  | True                             |
    | id       | 127b418dcfdf4d389a8f7f5fa6b15a8f |
    | name     | demo2                            |
    | username | demo2                            |
    +----------+----------------------------------+

Keystone, el componente de OpenStack encargado de la autenticación y
autorización, utiliza un mecanismo de control de acceso basado en
roles, en este caso lo que queremos es que el usuario "demo2" tenga el
rol "_member_" en el proyecto "demo2", para lo que hacemos:

    openstack role add --project demo2 --user demo2 _member_
    +-------+----------------------------------+
    | Field | Value                            |
    +-------+----------------------------------+
    | id    | 9fe2ff9ee4384b1894a90878d3e92bab |
    | name  | _member_                         |
    +-------+----------------------------------+

Puesto que no lo hemos hecho al crear el usuario, también podemos
definir una contraseña para este usuario:

    openstack user set --password OLAKASE demo2

Si fueramos a añadir varios usuarios, podríamos fácilmente agilizar
este proceso creando un shell script de forma bastante sencilla.