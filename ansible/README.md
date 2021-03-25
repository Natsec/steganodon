- [Installation du serveur](#installation-du-serveur)
- [Configuration avec Ansible](#configuration-avec-ansible)
  - [Authentification par clé SSH](#authentification-par-clé-ssh)
- [Matrice de flux du pare-feu du réseau](#matrice-de-flux-du-pare-feu-du-réseau)
- [NVIDIA](#nvidia)

# Configuration du serveur de calcul

>https://towardsdatascience.com/set-up-of-a-personal-gpu-server-for-machine-learning-with-ubuntu-20-04-100e787105ad

## Installation du serveur

Installer `Ubuntu Server 20 LTS` avec les options suivantes :
- Cocher l'installation d'un serveur SSH
- Compte utilisateur `user:user`

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

On peut lancer des commandes à distances avec :
```bash
ansible ubuntu -a "ls"
```

### Authentification par clé SSH

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

## Matrice de flux du pare-feu du réseau

| De / Vers |   Machine   |  VPN  |    Internet    |
| :-------: | :---------: | :---: | :------------: |
|  Machine  |      -      |       | DNS,HTTP,HTTPS |
|    VPN    |     SSH     |   -   |                |
| Internet  | Wake On Lan |       |       -        |

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
