- [Ansible](#ansible)
	- [Installation du serveur](#installation-du-serveur)
	- [Lancement du playbook Ansible](#lancement-du-playbook-ansible)

# Ansible
Rôle Ansible qui configure le serveur de calcul du projet.

## Installation du serveur
Installer `Ubuntu 20 Desktop` sur le serveur avec les options suivantes :
- compte utilisateur : `user:user`

Puis lancer les commandes suivantes :
```bash
# clavier en azerty
setxkbmap fr
echo 'setxkbmap fr' >> ~/.bashrc
sudo apt update
sudo apt upgrade
sudo apt install openssh-server
```

## Lancement du playbook Ansible

Lancer le playbook de puis la machine de contrôle :
```bash
# apt install ansible
ansible-playbook playbook.yml
```

On peut lancer des commandes à distances avec :
```
ansible ubuntu -a "ls"
```
