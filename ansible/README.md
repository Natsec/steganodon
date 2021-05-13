- [Installation du serveur](#installation-du-serveur)
- [Configuration avec Ansible](#configuration-avec-ansible)
- [Authentification par clé SSH](#authentification-par-clé-ssh)
- [Installation des drivers NVIDIA](#installation-des-drivers-nvidia)
- [Environnement virtuel python](#environnement-virtuel-python)

# Configuration du serveur de calcul

## Installation du serveur

Installer `Ubuntu Server 20 LTS` avec les options suivantes :
- Cocher l'installation d'un serveur SSH
- Compte utilisateur `user:user`

Matrice de flux du pare-feu du réseau :

| De / Vers |     Machine      |  VPN  |      Internet      |
| :-------: | :--------------: | :---: | :----------------: |
|  Machine  |        -         |       | DNS,HTTP,HTTPS,NTP |
|    VPN    | SSH, HTTP, HTTPS |   -   |                    |
| Internet  |   Wake On Lan    |       |         -          |

## Configuration avec Ansible

Rôle Ansible qui configure le serveur de calcul du projet.

Actions à faire avant le premier lancement de ansible, sur la machine de contrôle :
```bash
# copier les fichiers de cuDNN
scp cuda user@ubuntu:/tmp/cuda

ssh user@ubuntu
    # sur la machine distante
    sudo apt install python python-apt
```

Lancer le playbook depuis la machine de contrôle :
```bash
# apt install ansible sshpass
ansible-playbook playbook.yml
```

## Authentification par clé SSH

Générer une paire de clé sur la machine cliente :
```bash
ssh-keygen -f ~/.ssh/id_projet2a_natsec
```

Copier la clé publique vers le serveur :
```bash
ssh-copy-id -i ~/.ssh/id_projet2a_natsec.pub natsec@172.16.22.1
# OU
# copier la clé publique dans le fichier /home/natsec/.ssh/authorized_keys du serveur
```

Editer le fichier `~/.ssh/config` :
```
Host s serveur_de_calcul
    HostName 172.16.22.1
    IdentityFile ~/.ssh/id_projet2a_natsec
    User natsec
```

Quand la commande `ssh s` fonctionne, copier la clé publique dans le fichier `/roles/calcul_server/vars/main.yml`.

## Installation des drivers NVIDIA

Pour que le serveur utilise la carte NVIDIA pour faire ses calculs, les étapes sont :
1. installation des drivers de la carte graphique
2. installation de CUDA pour compiler des programmes pour GPU
3. installation de la librairie cuDNN qui facilite les calculs de réseau de neurone

Installation des drivers :
```bash
# afficher le matériel graphique
sudo apt install hwinfo
hwinfo --gfxcard --short
# afficher les drivers recommandés
sudo apt install ubuntu-drivers-common
sudo ubuntu-drivers devices
# installer les drivers recommandés
sudo ubuntu-drivers install
# redémarrer le serveur
sudo reboot
# afficher la version des drivers NVIDIA
sudo nvidia-smi
```

Installation de CUDA :
```bash
sudo apt install nvidia-cuda-toolkit
# afficher la version de CUDA et la noter (ex: 10.1)
nvcc --version
# compiler le fichier hello.cu pour tester le bon fonctionnement
cd /tmp; nvcc -o hello hello.cu && ./hello # si affiche Max error: 0.000000, c'est bon
```

Installation de cuDNN. Télécharger la version de cuDNN qui correspond à la version de CUDA sur https://developer.nvidia.com/rdp/cudnn-download.
```bash
# copier puis décomprésser l'archive
cd /tmp; tar -xzvf cudnn-10.1-linux-x64-v8.0.5.39.tgz
sudo cp /tmp/cuda/include/cudnn.h /usr/lib/cuda/include/
sudo cp /tmp/cuda/lib64/libcudnn* /usr/lib/cuda/lib64/
sudo chmod a+r /usr/lib/cuda/include/cudnn.h /usr/lib/cuda/lib64/libcudnn*
```

## Environnement virtuel python

Pour sortir de l'environnement virtuel python, faire `deactivate`.
