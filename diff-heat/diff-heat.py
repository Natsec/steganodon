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

channel = ["Red", "Green", "Blue", ""]
# for i in range(3):
# 	plt.figure("Channel {} : {}".format(i, channel[i]))
# 	plt.imshow(image1[:, :, i])
# 	plt.colorbar()


plt.show()

rows, cols = 2, 2
axes=[0]
fig=plt.figure()

for i in range(rows * cols):
    # rand_img = np.random.randint(255, size=(200, 200))
    axes.append(fig.add_subplot(rows, cols, i+1))
    if i < 3:
        subplot_title = "Channel {} : {}".format(i, channel[i])
        axes[-1].set_title(subplot_title)
        plt.imshow(image1[:, :, i])
    else:
        plt.imshow(image1)

    plt.colorbar()
    axes[-1].sharex(axes[-1])
    axes[-1].sharey(axes[-1])

fig.tight_layout()
plt.show()
