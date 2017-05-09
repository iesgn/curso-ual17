# Opciones de instalación de OpenStack

## Instalación manual

En primer lugar realizamos la instalación del sistema operativo en los
equipos que van a formar la nube de infraestructura y procedemos a
instalar OpenStack desde los repositorios propios de la distribución
elegida, siguiendo por ejemplo los pasos de la documentación oficial
de OpenStack:

* [OpenStack Documentation](http://docs.openstack.org/)

Obviamente debemos contar con el requisito previo que la versión de
OpenStack que queremos instalar esté empaquetada y disponible para esa
distribución, lo cual no es siempre posible ya que el ritmo de
desarrollo de OpenStack no siempre coincide con el de la distribución
en cuestión.

### Ubuntu

La solución ideada por Ubuntu para dar soporte a diferentes versiones
de Ubuntu y OpenStack ha sido utilizar unos repositorios específicos,
denominados ["The Ubuntu Cloud
Archive"](https://wiki.ubuntu.com/ServerTeam/CloudArchive),
principalmente válidos para instalar OpenStack sobre las versiones LTS
de Ubuntu. En estos momentos la opción más lógica sería utilizar
Ubuntu Trusty como sistema base y añadir el repositorio
correspondiente a la versión de OpenStack que quisiéramos utilizar,
por ejemplo:

    sudo add-apt-repository cloud-archive:kilo

Un aspecto importante a la hora de optar por una versión u otra de
OpenStack sobre ubuntu sería el soporte que va a tener dicha versión
en esta distro. De forma general, las versiones de OpenStack sólo
ofrecen soporte durante 18 meses, pero Ubuntu aumenta por su cuenta el
soporte para determinadas versiones (las que se publican con sus
versiones LTS) hasta los 5 años, tal como puede verse en la siguiente
imagen:

![Ubuntu OpenStack
 support](https://wiki.ubuntu.com/ServerTeam/CloudArchive?action=AttachFile&do=get&target=plan.png)

### Debian

Debian tiene un ritmo pausado de publicación, que no termina de
encajar con la frenética velocidad de publicación de OpenStack hasta
ahora. La versión disponible en Debian stable (jessie) es OpenStack
Icehouse y se está añadiendo soporte a versiones más modernas de
OpenStack sobre stable utilizando Debian backports. La versión de
OpenStack disponible en estos momentos en backports es Liberty.

La versión de OpenStack disponible en testing/sid suele coincidir con
la última versión de OpenStack disponible (salvo cuando Debian testing
pasa a frozen), pero por las características de testing/sid no son
versiones apropiadas para utilizar en producción.

### CentOS/Fedora

Dependiendo de la versión de la distribución utilizada, los paquetes
de OpenStack pueden inclurse ya empaquetados, pero en general habrá
que utilizar los repositorios del [proyecto
RDO](https://www.rdoproject.org/) que es el encargado de realizar el
empaquetado de OpenStack para Red Hat y derivadas (Fedora y CentOS),
para lo que habrá que añadir el repositorio de RDO para la versión
escogida y en el caso de CentOS también los repositorios EPEL:

    yum install
    http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
    yum install
    http://rdo.fedorapeople.org/openstack-kilo/rdo-release-kilo.rpm

El caso de Red Hat no lo vamos a contemplar, ya que utiliza su propio
mecanismo a través del producto [Red Hat Enterprise Linux OpenStack
Platform](https://www.redhat.com/es/technologies/linux-platforms/openstack-platform).

## Utilización de herramientas de gestión de la configuración

### Puppet

Existen manifiestos oficiales de puppet para OpenStack disponibles en
Github:

* [https://github.com/puppetlabs/puppetlabs-openstack](https://github.com/puppetlabs/puppetlabs-openstack)

Según lo descrito allí la última versión de OpenStack instalable con
los mismos es OpenStack Juno

### Chef

Las recetas oficiales de chef para la configuración de OpenStack están
dentro del proyecto OpenStack:

* [https://github.com/openstack/openstack-chef-repo](https://github.com/openstack/openstack-chef-repo)

Están preparadas para la instalación de OpenStack Liberty sobre Ubuntu
14.04 o CentOS 7

### Ansible

[OpenStack
Ansible](http://docs.openstack.org/developer/openstack-ansible/install-guide/)
es también parte del proyecto OpenStack y proporciona libros de
jugadas de ansible para la configuración de OpenStack utilizando
también LXC.

OpenStack-ansible está disponible para Icehouse, Juno, Kilo y Liberty.

## TripleO

TripleO siginifica OpenStack on OpenStack y es un componente de
OpenStack inicialmente desarrollado para desplegar OpenStack. TripleO
está pensado fundamentalmente para despliegues reales en centros de
datos, pero a medida que avanza el proyecto se va utilizando en
escenarios cada vez más variados.

TripleO monta un pequeño OpenStack, típicamente en un solo equipo y
que suele recibir el nombre de "undercloud". Los servidores (físicos o
virtuales) que van a formar parte del OpenStack que quiere implantarse
se instancia desde este OpenStack y suele denominarse "overcloud", en
el caso de tratarse de servidores físicos se utiliza el componentes
Ironic que permite gestionar servidores físicos como recursos de una
nube a través de IPMI, PXE y otras tecnologías.

[TripleO architecture overview](https://github.com/rbrady/tripleo/blob/master/docs/architecture_overview.rst)

## Distribuciones

Hay muchas distribuciones que utilizan uno o varios de los componentes
anteriores para facilitar la instalación de OpenStack, el listado de
las más conocidas es:

### RDO

Proyecto que proporciona paquetes y herramientas de instalación para
las distribuciones derivadas de Red Hat:

* Packstack: Conjunto de scripts que utilizan manifiestos de puppet
  para realizar la instalación.
* RDO Manager: Versión libre de RHE OSP Director

### Mirantis Fuel

Instalador muy sencillo desarrollado originalmente por la empresa
Mirantis, que ha sido incorporado al proyecto dentro del "Big Tent".

* [Mirantis OpenStack Releases](https://software.mirantis.com/releases/)

### Ubuntu OpenStack

Ubuntu ha desarrollado varias herramientas propias para facilitar o
complementar la instalación y configuración de OpenStack sobre Ubuntu:

* [Juju](http://www.ubuntu.com/cloud/juju) Es una herramienta de
  gestión de la configuración muy relacionada con cloud y ubuntu
* [MaaS](http://www.ubuntu.com/cloud/maas) Metal as a Service es un
  enfoque alternativo a la utilización de OpenStack TripleO para el
  despliegue de OpenStack en servidores físicos

## Enlaces interesantes

* [OpenStack distros](https://www.openstack.org/marketplace/distros/)
* [Mirantis OpenStack 7.0 vs Red Hat Enterprise Linux OpenStack
  Platform
  7](https://www.mirantis.com/blog/mirantis-openstack-7-0-vs-red-hat-rhel-openstack-platform-7/)

