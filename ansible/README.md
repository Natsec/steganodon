# Ansible

Rôle Ansible de configuration du serveur.

## Lancement
Avant de lancer le playbook, sur la machine de controle :
```
rm -f /root/.ssh/known_host* && ssh -T git@github.com
```

Pour finaliser :
```
maj && reboot
```
