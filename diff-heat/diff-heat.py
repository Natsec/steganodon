#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

"""
TODO: trois images dans une fenêtre

"""

image1 = img.imread(sys.argv[1])
# image2 = img.imread(sys.argv[2])

channel = ["Red", "Green", "Blue"]
for i in range(3):
	plt.figure("Channel {} : {}".format(i, channel[i]))
	plt.imshow(image1[:, :, i])
	plt.colorbar()


plt.show()
