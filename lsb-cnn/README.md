# LSB-CNN

- [Prerequisite](#prerequisite)
- [Usage](#usage)
- [Documentation](#documentation)

This python program trains a Convolutional Neural Network model to detect the use of Least Significant Bit steganography in a picture.

It makes the following tasks :
- loads images from a directory
- creates a CNN model
- trains the CNN model (or resumes it's training if checkpoints already exists)
- saves checkpoint during training
- saves the whole model at the end of the training
- records training data for TensorBoard

## Prerequisite

The arborescence of the `dataset` directory must be as follows :
```shell
dataset/
├── cover/
│   ├── img_1.png
│   ├── img_2.png
│   └── img_3.png
└── stego/
    ├── img_1.png
    ├── img_2.png
    └── img_3.png
```

The names of the directories just under `dataset` represent the label of the pictures just underneath them. So all pictures in the `cover` directory will be labelled as "cover" images.

## Usage

There is two ways of launching the program, which determines the name of the generated model and all it's associated data (checkpoint, saved model, training logs).

When lauched without any arguments, the name of the generated model will be the current date. When launched with an argument, the name of the generated model will be the current date plus the argument's value :
```bash
python3 lsb-cnn.py
# 20210331-133742

python3 lsb-cnn.py experimenting_with_more_layers
# 20210331-133742-experimenting_with_more_layers
```

Naming the models in such a way helps to keep track of the different versions of the models while experimenting with hyperparameters (aka playing with the knobs), and visualizing the learning curves in TensorBoard.

> If the script execution is aborted too soon (ex: before a certain amount of checkpoints was generated), the model's directory is deleted to keep the place clean.

## Documentation

To generate the documentation with pdoc :
```shell
pdoc --html .\lsb-cnn.py --output-dir doc --force
```

## Notes de test

Lancement de first_neural_network.py
sur laptop (cpu) :
