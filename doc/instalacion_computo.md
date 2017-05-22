# Instalación automática de nuevos nodos de computación con ansible

## Configuración inicial del nuevo nodo de computación

En primer lugar deshabilitamos la extensión `port security` de las dos redes del nuevo nodo:

	nova remove-secgroup compute2 default
	neutron port-update  <Port1_id> --port-security-enabled=False
	neutron port-update  <Port2_id> --port-security-enabled=False

Actualizamos el sistema e instalamos los paquetes necesarios:

	github/terraform-openstack/conf$ fab -H 172.22.200.62 main
	
## Modificación en la receta ansible

En el fichero `ansible_hosts` configuramos el nuevo nodo de computación:

	...
	[compute-nodes]
	compute2 ansible_ssh_host=172.22.200.62
	...

Creamos una nueva receta omputo.yml` con el siguiente contenido:

	---	

	- hosts: compute-nodes
	  roles:
	    - role: common	

	- hosts: compute-nodes
	  roles:
	    - role: openstackclient	

	- hosts: compute-nodes
	  roles: 
	    - role: openrc	

	- hosts: compute-nodes
	  roles:
	    - role: novacompute	

	- hosts: controller-nodes
	  roles:
	    - role: nova_init	

	- hosts: compute-nodes
	  roles:
	    - role: neutron-agents-compute	

	- hosts: controller-nodes
	  roles:
	    - role: restart-services

Y ejecutamos la receta:

	ansible-playbook computo.yml --sudo

## Comprobaciones finales

Desde el controlador:

	source admin_openrc.sh

	openstack hypervisor list
	+----+---------------------+-----------------+-------------+-------+
	| ID | Hypervisor Hostname | Hypervisor Type | Host IP     | State |
	+----+---------------------+-----------------+-------------+-------+
	|  1 | compute1            | QEMU            | 192.168.0.5 | up    |
	|  2 | compute2            | QEMU            | 192.168.0.7 | up    |
	+----+---------------------+-----------------+-------------+-------+



	nova service-list

	+----+------------------+------------+----------+---------+-------+----------------------------+-----------------+
	| Id | Binary           | Host       | Zone     | Status  | State | Updated_at                 | Disabled Reason |
	+----+------------------+------------+----------+---------+-------+----------------------------+-----------------+
	| 1  | nova-scheduler   | controller | internal | enabled | up    | 2017-05-09T08:55:54.000000 | -               |
	| 4  | nova-consoleauth | controller | internal | enabled | up    | 2017-05-09T08:55:51.000000 | -               |
	| 5  | nova-conductor   | controller | internal | enabled | up    | 2017-05-09T08:55:54.000000 | -               |
	| 6  | nova-compute     | compute1   | nova     | enabled | up    | 2017-05-09T08:55:53.000000 | -               |
	| 7  | nova-compute     | compute2   | nova     | enabled | up    | 2017-05-09T08:55:53.000000 | -               |
	+----+------------------+------------+----------+---------+-------+----------------------------+-----------------+

	neutron agent-list

	+--------------------------------------+--------------------+------------+-------------------+-------+----------------+---------------------------+
	| id                                   | agent_type         | host       | availability_zone | alive | admin_state_up | binary                    |
	+--------------------------------------+--------------------+------------+-------------------+-------+----------------+---------------------------+
	| 0eefb2f5-0ead-4ce1-83aa-5614d5894e09 | Metadata agent     | controller |                   | :-)   | True           | neutron-metadata-agent    |
	| 18c6a8a6-83a2-430e-8e5d-9318479475e2 | Open vSwitch agent | compute2   |                   | :-)   | True           | neutron-openvswitch-agent |
	| 22ac926f-6e07-4218-8d06-1123df1c4696 | DHCP agent         | controller | nova              | :-)   | True           | neutron-dhcp-agent        |
	| 30a157a1-b881-4b80-830a-91d9b0fc1033 | Open vSwitch agent | controller |                   | :-)   | True           | neutron-openvswitch-agent |
	| 745e96ee-e079-4b08-b2d3-f74fb6a2e1cf | Open vSwitch agent | compute1   |                   | :-)   | True           | neutron-openvswitch-agent |
	| d6a59875-6d4a-482b-a398-15b4000e17a7 | L3 agent           | controller | nova              | :-)   | True           | neutron-l3-agent          |
	+--------------------------------------+--------------------+------------+-------------------+-------+----------------+---------------------------+

