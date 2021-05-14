# TensorBoard

Pour lancer tensorboard en local :
```shell
tensorboard --logdir ./logs/ --port 80
# OU
sudo /opt/gpu_virtualenv/bin/tensorboard --logdir ./logs/ --port 443 --bind_all
```

Pour upload sur https://tensorboard.dev :
```shell
# upload
tensorboard dev upload --logdir ./logs/
# ajouter une description
tensorboard dev update-metadata --experiment_id to6cbfQcQNGOJr7NJ6rDlQ --name "Steganodon" --description "Premier TensorBoard du projet"
```
Aller sur https://tensorboard.dev/experiment/to6cbfQcQNGOJr7NJ6rDlQ/ pour voir.
