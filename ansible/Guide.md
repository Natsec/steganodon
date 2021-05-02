# Guide de déploiement et d'utilisation V0

L'objectif du projet STEGANODON est d'aider les enquêteurs forensics numériques à identifier rapidement la technique la plus probablement utilisée pour masquer des données dans une image.

Le produit final est un modèle de machine learning entraîné, avec lequel on intéragit via une applicaiton web.

Le document est divisé en 2 grandes parties. Tout d'abord, la partie déploiement du produit qui détaille déploiement du système pour entraîner le modèle de l'application. Puis, la partie utilisation du produit explique comment utiliser l'application.

## Déploiement du produit

Le système utilisé pour entraîner le modèle est un serveur équiper d'une carte graphique pour effectuer les calculs.

### Prérequis

Les  prérequis nécessaires avant de passer à la configuration du serveur de calcul sont :
- Ubuntu 20 LTS
- un compte `user:V@nnes56;` dans le groupe sudo
- Une connexion Internet

La carte graphique n'est pas obligatoire, mais elle permet d'accélérer le temps de calcul.

### Installation des pilotes de la carte graphique

On commence par installer les pilotes de la carte graphique. Pour notre projet, nous disposions d'une carte graphique Nvidia RTX 2070 6Go.

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

### Configuration du serveur de calcul

Pour le reste de la configuration, nous avons fait une recette Ansible qu'il suffit de lancer pour terminer la configuration.

Ce rôle effectue les tâches suivantes :
- réglage de l'heure
- installation des paquets utiles
- création des utilisateurs et du répertoire partagé
- configuration SSH
- finalisation de l'installation des pilots Nvidia (tâche qui ont pu être automatisées)
- configuration de l'environnement vituel de python

Ansible permet d'automatiser les tâches d'administration. Comme les tâches sont décrites avec une syntaxe relativement simple, les recettes (suite de tâches) constituent aussi une documentation de la configuration du serveur.

Pour récupérer la recette de configuration, il faut cloner le dépôt sur une machine autre que le serveur de calcul :
```bash
# cloner le dépôt
git clone https://github.com/Natsec/steganodon.git
# aller dans le répertoire ansible
cd steganodon/ansible
# installer ansible et sshpass
apt install ansible sshpass
# lancer la recette ansible
ansible-playbook playbook.yml
```

Le serveur de calcul est maintenant configuré.

### Récupération des fichiers de développement

Pour récupérer les fichiers de développement du modèle, on fait la même chose sur le serveur de calcul :
```bash
# cloner le dépôt
git clone https://github.com/Natsec/steganodon.git
# aller dans le répertoire de développement
cd steganodon/
```

C'est dans ce répertoire que se trouvent les fichiers qui effectuent l'entraînement du modèle.

### Génération du dataset

Le dataset est le jeu d'images qui va servir à entraîner le modèle. Nous commencons par récupérer des images "cover" qui ne sont pas stéganographiées.

Nous appliquons ensuite de la stéganographie sur ces images pour obtenir des images "stego".

## Utilisation du produit
