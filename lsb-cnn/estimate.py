"""Training of a CNN model for LSB steganography detection.

This python program trains a Convolutional Neural Network model to detect the use of Least Significant Bit steganography in a picture.

author : Kamil Mohoboob, Jean Jestin-Scanvion, Amaury Bonnaud

date : 03/03/2021
"""

import os
import argparse
import numpy as np
import PIL

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf


def get_image_path():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--image_path",
        dest="image_path",
        required=True,
        help="Path to image to evaluate",
    )
    return parser.parse_args().image_path


def main():
    image_path = get_image_path()
    print(image_path)

    # load the image
    print(f"Loading image {image_path}")
    image = PIL.Image.open(image_path)
    # convert image to numpy array
    image = np.array(image)
    print(image.shape)

    # chargement du modèle
    new_model = tf.keras.models.load_model("saved_model/lsb-cnn")

    # Evaluate the restored model
    estimation = new_model.predict(image)
    print(estimation)


if __name__ == "__main__":
    main()
