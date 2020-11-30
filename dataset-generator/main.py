#!/usr/bin/python3
#coding:utf-8

import random
import os

# ---------------------------------------

"""
	@role	:	piocher une citation aléatoirement dans dico.txt
	@param	:	NONE
	@return	:	la citation piochée
"""
def get_random_text():
	with open("dico.txt") as dico:
		return random.choice(dico.readlines()).strip()

# ---------------------------------------

"""
	@role	:	créer un fichier temporaire contenant l'information à dissimuler
	@param	:	le fichier temporaire à créer ; le texte à écrire dans ce fichier
	@return	:	NONE
"""
def set_text_file(temp_text_file, data_to_hide):
	with open(temp_text_file, "w") as file:
		file.write(data_to_hide)

# ---------------------------------------

"""
	@role	:	stéganographier les données texte dans une image
	@param	:	l'image cover ; le fichier texte à dissimuler ; l'image stego
	@return	:	NONE
"""
def stego_lsb(cover_image, text_file, stego_image):
	steg_cmd = os.system("stegolsb steglsb -h -i {} -s {} -o {}".format(cover_image, text_file, stego_image))

	if steg_cmd != 0:
		raise Exception("Steg LSB failed! \n [Install] : \n\t* git clone https://github.com/ragibson/Steganography \n\t * cd Steganography \n\t * python3 setup.py install \n\n")

# ---------------------------------------

if __name__ == '__main__':
	# répertoires des images cover et stego
	cover_images_dir = "./cover-images"
	stego_images_dir = "./stego-images"

	# fichier temporaire contenant le texte à dissimuler
	temp_text_file = "./tmp.txt"

	try:
		# vérification de l'existance des dossiers d'images
		if not os.path.isdir(cover_images_dir):
			raise Exception("Cover images directory was not found!")

		if not os.path.isdir(stego_images_dir):
			raise Exception("Stego images directory was not found!")

		# stégo de chaque image cover avec un texte aléa
		for cover_image in os.listdir(cover_images_dir):
			stego_image = "{}/lsb_{}".format(stego_images_dir, cover_image)
			cover_image = "{}/{}".format(cover_images_dir, cover_image)

			if not os.path.isfile(cover_image):
				raise Exception("[{}] was not found in cover imges directory!".format(cover_image))

			# définition d'un texte secret aléatoire
			data_to_hide = get_random_text()

			# création d'un fichier temporaire contenant le texte à dissimuler
			set_text_file(temp_text_file, data_to_hide)

			# stéganographie du texte aléa dans l'image
			stego_lsb(cover_image, temp_text_file, stego_image)
	except Exception as e:
		print(e)
	else:
		print("\n***************\nProcess done!\n***************")
	finally:
		if os.path.isfile(temp_text_file):
			os.remove(temp_text_file)
