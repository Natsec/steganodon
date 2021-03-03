"""Entraînement d'un CNN pour la détection de LSB.

Ce programme python effectue l'entraînement d'un modèle de réseau de neurones convolutif.

Il effectue les tâches suivantes :
    - chargement des images à partir d'un répertoire
    - création d'un modèle CNN
    - entraînement du modèle
    - enregistrement de checkpoints au cours de l'entraînement
    - enregistrement du modèle entraîné à la fin
    - enregistrement des données d'entraînement pour tensorboard

author :
    - Kamil Mohoboob
    - Jean Jestin-Scanvion
    - Amaury Bonnaud

date   :
    03/03/2021
"""

from tensorflow import keras
import numpy as np
import os
import pathlib
import tensorflow as tf
import tensorflow_datasets as tfds


print("tensorflow version :", tf.__version__)


########################################
# Chargement du dataset
########################################

data_dir = tf.keras.utils.get_file(
    origin=dataset_url, fname="flower_photos", untar=True
)
data_dir = pathlib.Path(data_dir)
"""str: Chemin du répertoire contenant les images du dataset."""

# compter le dataset
image_count = len(list(data_dir.glob("*/*.jpg")))
"""int: Nombre d'images du dataset"""
print(f"Le dataset contient {image_count} images.")

batch_size = 32
img_height = 180
"""int: Hauteur des images en pixel."""
img_width = 180
"""int: Largeur des images en pixel."""
# charger le dataset en mémoire (images d'entraînement)
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size,
)
"""obj: Images retenues pour l'entraînement."""
# charger le dataset en mémoire (images d'évaluation)
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size,
)
"""obj: Images retenues pour la validation du modèle."""
# afficher les labels
class_names = train_ds.class_names
"""list: Nom des classes d'images."""
print(f"Labels : {class_names}")

# mise en cache des données pour améliorier les performances
# https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle#answer-48096625
SIZE = int(image_count * 1.1)
train_ds = train_ds.cache().prefetch(buffer_size=SIZE)
"""obj: Images d'entraînement mises en cache."""
val_ds = val_ds.cache().prefetch(buffer_size=SIZE)
"""obj: Images de validation mises en cache."""


########################################
# Création du modèle
########################################

model = tf.keras.Sequential(
    [
        # normalisation des données (d'un intervalle [0;255] à [0;1])
        layers.experimental.preprocessing.Rescaling(1.0 / 255),
        # convolutions
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPooling2D(),
        # couches denses
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        # classification dans 2 classes (stego/clean)
        layers.Dense(2),
    ]
)
"""obj: Modèle de réseau de neurones convolutif."""

# affichage du résumé du modèle
model.summary()

# compilation du modèle
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)


########################################
# Configuration des checkpoints
########################################

checkpoint_path = "checkpoints/cp.ckpt"
"""str: Chemin relatif du répertoire qui contient les checkpoints."""

# TODO : si un checkpoint existe on le charge
if "checkpoint exist":
    new_model.load_weights(checkpoint_path)
# sinon on le configure
else:
    checkpoint_dir = os.path.dirname(checkpoint_path)
    """str: Chemin complet du répertoire qui contient les checkpoints."""

    # création d'un callback qui enregistrera les poids du modèle
    cp_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_path, save_weights_only=True, verbose=1
    )
    """obj: Fonction qui sera appelée pour sauvegarder l'état de l'entraînement après chaque période."""
    # This may generate warnings related to saving the state of the optimizer.
    # These warnings (and similar warnings throughout this notebook)
    # are in place to discourage outdated usage, and can be ignored.


########################################
# Configuration de Tensorboard
########################################

# création d'un callback qui enregistrera les log pour tensorboard
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
"""str: Chemin relatif du répertoire qui contient les logs d'entraînement utilisés par TensorBoard."""
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
"""ojb: Fonction qui sera appelée pour enregistrer les logs d'entraînement après chaque période."""

########################################
# Entraînement du modèle
########################################

model.fit(
    train_images,
    train_labels,
    epochs=10,
    validation_data=(test_images, test_labels),
    callbacks=[cp_callback, tensorboard_callback],
)


########################################
# Enregistrement du modèle
########################################

# Enregistre le modèle entier, permet l'import dans tensorflow.js
new_model.save("saved_model/lsb-cnn")
