"""
This script allows the user to generate a stego dataset from cover images with random secret text to be hidden in the file.

This tool accepts BMP and PNG files.

This script requires that [LSBSteg](https://github.com/ragibson/Steganography) be installed within the Python
environment you are running this script in.
"""

import random
import os
import subprocess

# ---------------------------------------

def get_random_text():
	"""Gets and returns a random text to be hidden with Steganography.

    Returns:
	- **(str)**: A string that contains a random text comming from a local file.
    """

	with open("dico.txt") as dico:
		return random.choice(dico.readlines()).strip()

# ---------------------------------------

def set_text_file(temp_text_file, data_to_hide):
	"""Creates a file and writes given text into it.

    Args:
	    temp_text_file (str): The temporary file to contain the secret text.
	    data_to_hide (str): The secret to write into the temporary file.
    """

	with open(temp_text_file, "w") as file:
		file.write(data_to_hide)

# ---------------------------------------

def stego_lsb(cover_image, text_file, stego_image):
	"""Steganographies a random text within a cover image to create a stego image.

    Args:
	    cover_image (str): The source image filename.
	    text_file (str): The filename containg the secret.
	    stego_image (str): The destination image filename.
    """

	steg_cmd_output = subprocess.check_output(["stegolsb", "steglsb", "-h", "-i", cover_image, "-s", text_file, "-o", stego_image])
	print(steg_cmd)

	if steg_cmd_output:
		raise Exception("Steg LSB failed! \n [Install] : \n\t* git clone https://github.com/ragibson/Steganography \n\t * cd Steganography \n\t * python3 setup.py install \n\n")

# ---------------------------------------

def main():
	"""Runs the dataset generator program when executing the script from the command-line."""

	# directories that contain cover images and future stego images
	cover_images_dir = "./cover-images"
	stego_images_dir = "./stego-images"

	# temporary file that will contain a random text to be hidden within an image
	temp_text_file = "./tmp.txt"

	try:
		# files existance checks
		if not os.path.isdir(cover_images_dir):
			raise Exception("Cover images directory was not found!")

		if not os.path.isdir(stego_images_dir):
			os.mkdir(stego_images_dir)

		# for each image do stego with random text
		for cover_image in os.listdir(cover_images_dir):
			stego_image = "{}/lsb_{}".format(stego_images_dir, cover_image)
			cover_image = "{}/{}".format(cover_images_dir, cover_image)

			if not os.path.isfile(cover_image):
				raise Exception("[{}] was not found in cover imges directory!".format(cover_image))

			# get a random string from file
			data_to_hide = get_random_text()

			# create a temporary file that will contain the random text
			set_text_file(temp_text_file, data_to_hide)

			# stego the cover image with the random text to create a new stego image
			stego_lsb(cover_image, temp_text_file, stego_image)
	except Exception as e:
		print(e)
	else:
		print("\n***************\nProcess done!\n***************")
	finally:
		if os.path.isfile(temp_text_file):
			os.remove(temp_text_file)

# ---------------------------------------

if __name__ == '__main__':
	main()
