# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.contrib.files import exists
env.user   = "ubuntu"
   

def main():
    
    
    put('sources.list','/etc/apt/sources.list',use_sudo=True)
    # Actualizar el sistema
    sudo("apt-get update")
    sudo("apt-get -y upgrade")
    sudo("apt-get install -y apt-transport-https")
    sudo("curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -")
    put('kubernetes.list','/etc/apt/sources.list.d/kubernetes.list',use_sudo=True)
    sudo("apt-get install  --allow-unauthenticated docker-engine")
    sudo("apt-get install -y kubelet kubeadm kubectl kubernetes-cni")
