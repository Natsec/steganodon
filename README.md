<p align="center">
<img width="80px" src="https://image.flaticon.com/icons/svg/921/921887.svg" alt="logo">
</p>

# STEGANODON : Deep Learning for steganalysis

The goal of the STEGANODON project is to help digital forensic investigators to rapidly identify which technique was most probably used to hide data in a picture.

This repo contains the following tools :
- [Diff-Heat](https://github.com/Natsec/steganodon/tree/master/diff-heat#diff-heat) : Visualizing differences between two pictures
- Data-Gen : Generating custom datasets to train our models
- an Ansible role to configure the server used to train our models

## Current research

Current research on blind steganalysis focus on **very accurate** neural networks models to detect the use of **one, very good steganographic algorithm**.

Our second year school project focus on training a **accurate enough** model to detect the most likely used technique among **several, simple steganographic algorithms**.

<!-- The following illustration gives a better picture : -->

The purpose of such a model, is to give the user a rapid overview of the research path with the best success potential during his investigation. Examples of usage case includes :
- Digital forensic analyst trying to find interesting picture among hundreds during an investigation 🕵️‍♀️
- CTF player trying to guess which steganographic technique was used on a picture 😉

## Datasets

The following table present the different dataset we are going to use :

| Jeu de données | Nombre, dimensions, couleur, format | Remarques                                                  | Source                                                                                              |
| -------------- | ----------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| BOSS           | 9 074 512x512 greyscale PGM         | 2 camera models                                            | [agents.fel.cvut.cz](http://agents.fel.cvut.cz/boss/index.php?mode=VIEW&tmpl=materials)             |
| ALASKA2        | 75 000 512x512 RGB JPG              | 40+ camera models                                          | [alaska.utt.fr](https://alaska.utt.fr/)                                                             |
| IStego100K     | 100 000 1024x1024 RGB JPG           | 30+ camera models                                          | [groundai.com](https://www.groundai.com/project/istego100k-large-scale-image-steganalysis-dataset/) |
| DGen-1         | 10 000 512x512 greyscale PNG        | Des images uniformes facileteront la distinction du bruit. | TEAM-06                                                                                             |
| DGen-2         | 10 000 variable greyscale PNG       | La taille variable introduira une nouvelle fonctionnalité. | TEAM-06                                                                                             |
| DGen-3         | 10 000 variable grey/RGB PNG        | La couleur introduira une nouvelle fonctionnalité.         | TEAM-06                                                                                             |
| DGen-4         | 10 000 variable grey/RGB PNG/JPG    | Le format d'image introduira une nouvelle fonctionnalité.  | TEAM-06                                                                                             |

## Development

We use [TensorFlow](https://www.tensorflow.org/) framework to develop our models.

We use [TensorBoard](https://www.tensorflow.org/tensorboard) to Visualize our model trainings. The board of our project is located [here](https://tensorboard.dev/experiment/to6cbfQcQNGOJr7NJ6rDlQ/#scalars).
