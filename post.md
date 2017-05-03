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

    openstack network create ext-net
    +---------------------------+--------------------------------------+
    | Field                     | Value                                |
    +---------------------------+--------------------------------------+
    | admin_state_up            | UP                                   |
    | availability_zone_hints   |                                      |
    | availability_zones        |                                      |
    | created_at                | 2017-05-03T16:42:12Z                 |
    | description               |                                      |
    | dns_domain                | None                                 |
    | id                        | a5d28859-889e-49e2-933a-0323dea671a6 |
    | ipv4_address_scope        | None                                 |
    | ipv6_address_scope        | None                                 |
    | is_default                | None                                 |
    | mtu                       | 1450                                 |
    | name                      | ext-net                              |
    | port_security_enabled     | True                                 |
    | project_id                | cc5c6e16149c4e1ea42753e11cbb6ede     |
    | provider:network_type     | vxlan                                |
    | provider:physical_network | None                                 |
    | provider:segmentation_id  | 65587                                |
    | qos_policy_id             | None                                 |
    | revision_number           | 3                                    |
    | router:external           | Internal                             |
    | segments                  | None                                 |
    | shared                    | False                                |
    | status                    | ACTIVE                               |
    | subnets                   |                                      |
    | updated_at                | 2017-05-03T16:42:12Z                 |
    +---------------------------+--------------------------------------+

A continuación definimos una subred donde aparece la definición lógica
de la red y cuyos valores dependerán de la red privada o pública a la
que esté conectada. En este caso el equipo está conectado a la red
192.168.1.0/24 con la puerta de enlace 192.168.1.1 y vamos a utilizar
el segmento 192.168.1.150-192.168.1.160 para las direcciones IP
flotantes de las instancias que correran sobre OpenStack:

    openstack subnet create --network ext-net --subnet-range 10.0.0.0/24 --allocation-pool start=10.0.0.100,end=10.0.0.254 --no-dhcp --gateway 10.0.0.1 ext-subnet
    +-------------------+--------------------------------------+
    | Field             | Value                                |
    +-------------------+--------------------------------------+
    | allocation_pools  | 10.0.0.100-10.0.0.254                |
    | cidr              | 10.0.0.0/24                          |
    | created_at        | 2017-05-03T16:49:30Z                 |
    | description       |                                      |
    | dns_nameservers   |                                      |
    | enable_dhcp       | False                                |
    | gateway_ip        | 10.0.0.1                             |
    | host_routes       |                                      |
    | id                | b32a5cc1-6af7-43e7-94da-ad0e6e56be18 |
    | ip_version        | 4                                    |
    | ipv6_address_mode | None                                 |
    | ipv6_ra_mode      | None                                 |
    | name              | ext-subnet                           |
    | network_id        | a5d28859-889e-49e2-933a-0323dea671a6 |
    | project_id        | cc5c6e16149c4e1ea42753e11cbb6ede     |
    | revision_number   | 2                                    |
    | segment_id        | None                                 |
    | service_types     |                                      |
    | subnetpool_id     | None                                 |
    | updated_at        | 2017-05-03T16:49:30Z                 |
    +-------------------+--------------------------------------+

### creación de un sabor

    openstack flavor create --id 0 --vcpus 1 --ram 64 --disk 1 m1.nano
    +----------------------------+---------+
    | Field                      | Value   |
    +----------------------------+---------+
    | OS-FLV-DISABLED:disabled   | False   |
    | OS-FLV-EXT-DATA:ephemeral  | 0       |
    | disk                       | 1       |
    | id                         | 0       |
    | name                       | m1.nano |
    | os-flavor-access:is_public | True    |
    | properties                 |         |
    | ram                        | 64      |
    | rxtx_factor                | 1.0     |
    | swap                       |         |
    | vcpus                      | 1       |
    +----------------------------+---------+


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

### Creación del router y una red interna en el protecto demo

Cargamos las credenciales del usuario demo:

    source demo_openrc.sh