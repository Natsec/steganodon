#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from scipy import stats


# ouverture de la première image
image1 = img.imread(sys.argv[1])
image1 = np.array(image1*255).astype(np.uint8)

# affichage des stats de la première image
print("Mean :                {}".format(np.mean(image1.flatten())))
print("Median :              {}".format(np.median(image1.flatten())))
print("Mode :                {}".format(stats.mode(image1.flatten())))
print("Standard deviation o: {}".format(np.std(image1.flatten())))
print("Variance o²:          {}".format(np.var(image1.flatten())))

# si deux images sont données en paramètre
if len(sys.argv) > 2:
    image2 = img.imread(sys.argv[2])
    image2 = np.array(image2*255).astype(np.uint8)

    # calcul des differences
    image_to_show = np.bitwise_xor(image1, image2)
else:
    image_to_show = image1

channel = ["Red", "Green", "Blue", "Alpha"]
height, width, chan = np.shape(image_to_show)

# paramétrage en fonction du format de l'image (JPG ou PNG)
if chan == 3:
    rows, cols = 2, 2
elif chan == 4:
    rows, cols = 2, 3


axe = [None, None, None, None, None]
fig = plt.figure()
for i in range(chan+1):
    # rand_img = np.random.randint(255, size=(200, 200))
    axe[i] = plt.subplot(rows, cols, i+1, sharex=axe[0], sharey=axe[0])
    if i < chan:
        subplot_title = "Channel {} : {}".format(i, channel[i])
        plt.imshow(image_to_show[:, :, i])
    else:
        subplot_title = "Full Color"
        plt.imshow(image_to_show)

    axe[i].set_title(subplot_title)
    plt.colorbar()

fig.tight_layout()
plt.show()
