"""Training of a CNN model for LSB steganography detection.

This python program trains a Convolutional Neural Network model to detect the use of Least Significant Bit steganography in a picture.

author : Kamil Mohoboob, Jean Jestin-Scanvion, Amaury Bonnaud

date : 03/03/2021
"""

from tensorflow import keras
import numpy as np
import os
import pathlib
import tensorflow as tf

# import tensorflow_datasets as tfds
import builtins


def print(*args):
    """Override of the builtin print function.

    This function prints text in color for better visibility.

    Args:
        *args (obj): Variable number of argument without keywords.
    """
    builtins.print("\033[34m[INFO] ", end="")
    builtins.print(*args)
    builtins.print("\033[0m", end="")


def load_dataset(data_dir, img_size):
    """Loads the dataset in memory.

    This function deduces the different classes of pictures from the directory structure, and load them in memory to improve performance.

    Args:
        data_dir (str): Relative path of the directory containing the dataset.
        img_size (tuple): Dimension of the training pictures in pixel.

    Returns:
        train_ds (obj): Training pictures loaded in memory.
        val_ds (obj): Validation pictures loaded in memory.
        class_names (list): Labels of the pictures.
    """

    data_dir = pathlib.Path(data_dir)
    """str: Relative path of the directory containing the dataset."""

    # compter le dataset
    image_count = len(list(data_dir.glob("*/*.jpg")))
    """int: Number of pictures in the dataset."""
    print(f"Le dataset contient {image_count} images.")

    batch_size = 32

    # charger le dataset en mémoire (images d'entraînement)
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=img_size,
        batch_size=batch_size,
    )
    """obj: Pictures used for training the model."""

    # charger le dataset en mémoire (images d'évaluation)
    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
    )
    """obj: Pictures used for validation of the model."""

    # afficher les labels
    class_names = train_ds.class_names
    """list: Class name of the pictures."""
    print(f"Labels : {class_names}")

    # mise en cache des données pour améliorier les performances
    # https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle#answer-48096625
    SIZE = int(image_count * 1.1)
    train_ds = train_ds.cache().prefetch(buffer_size=SIZE)
    """obj: Cached training pictures."""
    val_ds = val_ds.cache().prefetch(buffer_size=SIZE)
    """obj: Cached validation pictures."""

    return train_ds, val_ds, class_names


def main():
    print(f"TensorFlow version : {tf.__version__}")

    # ----------------------------------------
    # Chargement du dataset
    # ----------------------------------------

    train_images, test_images, labels = load_dataset("dataset", (180, 180))

    # ----------------------------------------
    # Création du modèle
    # ----------------------------------------

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
    """obj: Convolutional Neural Network model."""

    # affichage du résumé du modèle
    model.summary()

    # compilation du modèle
    model.compile(
        optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"],
    )

    # ----------------------------------------
    # Configuration des checkpoints
    # ----------------------------------------

    checkpoint_path = "checkpoints/cp.ckpt"
    """str: Relatif path of the directory containing the checkpoints."""

    # TODO : si un checkpoint existe on le charge
    if "checkpoint exist":
        new_model.load_weights(checkpoint_path)
    # sinon on le configure
    else:
        checkpoint_dir = os.path.dirname(checkpoint_path)
        """str: Full path of the directory containing the checkpoints."""

        # création d'un callback qui enregistrera les poids du modèle
        cp_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_path, save_weights_only=True, verbose=1
        )
        """obj: Function that will be called to save the training state of the model after each epoch."""
        # This may generate warnings related to saving the state of the optimizer.
        # These warnings (and similar warnings throughout this notebook)
        # are in place to discourage outdated usage, and can be ignored.

    # ----------------------------------------
    # Configuration de Tensorboard
    # ----------------------------------------

    # création d'un callback qui enregistrera les log pour tensorboard
    log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    """str: Relative path of the directory containing training logs used by TensorBoard."""
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=log_dir, histogram_freq=1
    )
    """ojb: Function that will be called to save training logs after each epoch."""

    # ----------------------------------------
    # Entraînement du modèle
    # ----------------------------------------

    model.fit(
        train_images,
        labels,
        epochs=10,
        validation_data=(test_images, labels),
        callbacks=[cp_callback, tensorboard_callback],
    )

    # ----------------------------------------
    # Enregistrement du modèle
    # ----------------------------------------

    # Enregistre le modèle entier, permet l'import dans tensorflow.js
    new_model.save("saved_model/lsb-cnn")


if __name__ == "__main__":
    main()
