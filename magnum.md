https://docs.openstack.org/developer/magnum/userguide.html

wget https://fedorapeople.org/groups/magnum/fedora-atomic-latest.qcow2

source admin_openrc.sh

openstack image create --disk-format=qcow2 --container-format=bare --file=fedora-atomic-latest.qcow2 --property os_distro='fedora-atomic' --public fedora-atomic-latest 


openstack flavor create --id 1 --vcpus 1 --ram 512 --disk 10 m1.tiny

source demo_openrc.sh

magnum cluster-template-create --name kubernetes-cluster-template \
--image fedora-atomic-latest \
--keypair clave \
--external-network ext-net \
--dns-nameserver 192.168.102.2 \
--master-flavor m1.tiny \
--flavor m1.tiny \
--coe kubernetes \
--fixed-network demo-net \
--fixed-subnet demo-subnet

+-----------------------+--------------------------------------+
| Property              | Value                                |
+-----------------------+--------------------------------------+
| insecure_registry     | -                                    |
| labels                | {}                                   |
| updated_at            | -                                    |
| floating_ip_enabled   | True                                 |
| fixed_subnet          | -                                    |
| master_flavor_id      | m1.tiny                              |
| uuid                  | b175bc39-29c2-40b2-b635-f9da25c3d7e1 |
| no_proxy              | -                                    |
| https_proxy           | -                                    |
| tls_disabled          | False                                |
| keypair_id            | atomic                               |
| public                | False                                |
| http_proxy            | -                                    |
| docker_volume_size    | -                                    |
| server_type           | vm                                   |
| external_network_id   | ext-net                              |
| cluster_distro        | fedora-atomic                        |
| image_id              | fedora-atomic-latest                 |
| volume_driver         | -                                    |
| registry_enabled      | False                                |
| docker_storage_driver | devicemapper                         |
| apiserver_port        | -                                    |
| name                  | kubernetes-cluster-template          |
| created_at            | 2017-05-08T07:22:54+00:00            |
| network_driver        | flannel                              |
| fixed_network         | -                                    |
| coe                   | kubernetes                           |
| flavor_id             | m1.tiny                              |
| master_lb_enabled     | False                                |
| dns_nameserver        | 192.168.102.2                        |
+-----------------------+--------------------------------------+


magnum cluster-template-list
+--------------------------------------+-----------------------------+
| uuid                                 | name                        |
+--------------------------------------+-----------------------------+
| b175bc39-29c2-40b2-b635-f9da25c3d7e1 | kubernetes-cluster-template |
+--------------------------------------+-----------------------------+

magnum cluster-create --name kubernetes-cluster \
--cluster-template kubernetes-cluster-template \
--master-count 1 \
--node-count 1


curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

