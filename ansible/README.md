- [Ansible](#ansible)
	- [Installation du serveur](#installation-du-serveur)
	- [Matrice de flux du pare-feu du réseau](#matrice-de-flux-du-pare-feu-du-réseau)
	- [Lancement du playbook Ansible](#lancement-du-playbook-ansible)
	- [Wake on Lan](#wake-on-lan)
	- [NVIDIA](#nvidia)

# Ansible
Rôle Ansible qui configure le serveur de calcul du projet.

>https://towardsdatascience.com/set-up-of-a-personal-gpu-server-for-machine-learning-with-ubuntu-20-04-100e787105ad

## Installation du serveur
Installer `Ubuntu Server 20 LTS` sur le serveur avec les options suivantes :
- Cocher l'installation d'un serveur SSH
- Compte utilisateur `user:userpass`

## Matrice de flux du pare-feu du réseau

| De / Vers |   Machine   |  VPN  |    Internet    |
| :-------: | :---------: | :---: | :------------: |
|  Machine  |      -      |       | DNS,HTTP,HTTPS |
|    VPN    |     SSH     |   -   |                |
| Internet  | Wake On Lan |       |       -        |

## Lancement du playbook Ansible

Lancer le playbook de puis la machine de contrôle :
```bash
# copier les fichiers de cuDNN
scp cuda user@ubuntu:/tmp/cuda
# apt install ansible
ansible-playbook playbook.yml
```

On peut lancer des commandes à distances avec :
```bash
ansible ubuntu -a "ls"
```

## Wake on Lan
Le WOL doit être activé dans le BIOS.
Et le routeur doit faire relai wol (et arp statique ?).

Pour tester depuis son pc :
```bash
# apt install wakeonlan
# en utilisant l'adresse de broadcast locale
wakeonlan -i 255.255.255.255 30:9c:23:ac:5d:39
# en utilisant l'adresse de broadcast d'un subnet
wakeonlan -i 192.168.0.255 30:9c:23:ac:5d:39
```

## NVIDIA

Pour afficher la version des drivers NVIDIA :
```bash
nvidia-smi
```

Pour tester que CUDA fonctionne :
```bash
cd roles/ai_server/files
nvcc -o test test.cu && ./test
# ‘Max error: 0.000000’ means your CUDA libraries are working as expected!
```

Pour afficher la version de CUDA :
```bash
nvcc --version
```
Télécharger la version de cuDNN qui correspond à la version de CUDA sur https://developer.nvidia.com/rdp/cudnn-download.
