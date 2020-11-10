- [Ansible](#ansible)
	- [Installation du serveur](#installation-du-serveur)
- [Matrice de flux du pare-feu du réseau](#matrice-de-flux-du-pare-feu-du-réseau)
	- [Lancement du playbook Ansible](#lancement-du-playbook-ansible)

# Ansible
Rôle Ansible qui configure le serveur de calcul du projet.

## Installation du serveur
Installer `Ubuntu Server 20 LTS` sur le serveur avec les options suivantes :
- Compte utilisateur : `user:user` ;
- Puis lancer les commandes suivantes :
```bash
# clavier en azerty
setxkbmap fr
echo 'setxkbmap fr' >> ~/.bashrc
sudo apt update
sudo apt upgrade
sudo apt install openssh-server
```

# Matrice de flux du pare-feu du réseau

| De / Vers |   Machine    |  VPN  |    Internet    |
| :-------: | :----------: | :---: | :------------: |
|  Machine  |      -       |       | DNS,HTTP,HTTPS |
|    VPN    |     SSH      |   -   |                |
| Internet  | Wake On Lan* |       |       -        |

## Lancement du playbook Ansible

Lancer le playbook de puis la machine de contrôle :
```bash
# apt install ansible
ansible-playbook playbook.yml
```

On peut lancer des commandes à distances avec :
```bash
ansible ubuntu -a "ls"
```
