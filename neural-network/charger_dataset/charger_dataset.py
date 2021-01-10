# https://www.tensorflow.org/tutorials/load_data/images

import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf

# pip install tensorflow_datasets
import tensorflow_datasets as tfds

print(tf.__version__)


# télécharger le dataset
import pathlib

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file(
    origin=dataset_url, fname="flower_photos", untar=True
)
data_dir = pathlib.Path(data_dir)

# compter le dataset
image_count = len(list(data_dir.glob("*/*.jpg")))
print(image_count)

# afficher une image
roses = list(data_dir.glob("roses/*"))
PIL.Image.open(str(roses[0]))


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
print(class_names)


# visualiser les données
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")

# mise en cache des données pour améliorier les performances
# https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle#answer-48096625
SIZE = int(image_count * 1.1)
train_ds = train_ds.cache().prefetch(buffer_size=SIZE)
val_ds = val_ds.cache().prefetch(buffer_size=SIZE)

# création du modèle
num_classes = 5
from tensorflow.keras import layers

model = tf.keras.Sequential(
    [
        layers.experimental.preprocessing.Rescaling(1.0 / 255),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(num_classes),
    ]
)

# compilation du modèle
model.compile(
    optimizer="adam",
    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)

# entraînement du modèle
model.fit(train_ds, validation_data=val_ds, epochs=3)
