# Dataset Generator

This python script is aimed to generate a stego images dataset from a cover images dataset.

## Prerequisite

Before to start with this tool you need first to install a Python module in order to achieve the stego process:

```bash
git clone https://github.com/ragibson/Steganography
cd Steganography
python3 setup.py install
```

## Usage


The first step is to get any dataset from the net and store all of its images into `./cover-images` directory as follow:

```bash
./cover-images
	img1.png
	img2.png
	img3.png
	...
```

Then your script is ready to be used:

```bash
./main.py
```

This will create the `./stego-images` directory with all the stego images.
