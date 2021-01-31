"""
author : KMO, ABO, JJE
date   : 31/01/2021
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

# compter le dataset
image_count = len(list(data_dir.glob("*/*.jpg")))
print(image_count)

batch_size = 32
img_height = 180
img_width = 180
# charger le dataset en mémoire (images d'entraînement)
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size,
)
# charger le dataset en mémoire (images d'évaluation)
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size,
)
# afficher les labels
class_names = train_ds.class_names
print("labels :", class_names)

# mise en cache des données pour améliorier les performances
# https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle#answer-48096625
SIZE = int(image_count * 1.1)
train_ds = train_ds.cache().prefetch(buffer_size=SIZE)
val_ds = val_ds.cache().prefetch(buffer_size=SIZE)


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

# TODO : si un checkpoint existe on le charge
if "checkpoint exist":
    new_model.load_weights(checkpoint_path)
# sinon on le configure
else:
    checkpoint_dir = os.path.dirname(checkpoint_path)

    # création d'un callback qui enregistrera les poids du modèle
    cp_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_path, save_weights_only=True, verbose=1
    )
    # This may generate warnings related to saving the state of the optimizer.
    # These warnings (and similar warnings throughout this notebook)
    # are in place to discourage outdated usage, and can be ignored.


########################################
# Configuration de Tensorboard
########################################

# création d'un callback qui enregistrera les log pour tensorboard
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)


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
