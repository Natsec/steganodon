# https://www.tensorflow.org/tutorials/keras/classification

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print("\nTensorflow version : {}".format(tf.__version__))
print("Built with CUDA : {}\n".format((tf.test.is_built_with_cuda())))
# exit(0)
tf.test.Benchmark()
#######################################
# Import the Fashion MNIST dataset
#######################################

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


#######################################
# Explore the data
#######################################

print(train_images.shape)
print(test_images.shape)


#######################################
# Preprocess the data
#######################################

# plt.figure()
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

# normalisation : passage de valeurs [0..255] à [0..1]
train_images = train_images / 255.0
test_images = test_images / 255.0

# affichage pour vérifier
# plt.figure(figsize=(10,10))
# for i in range(25):
# 	plt.subplot(5,5,i+1)
# 	plt.xticks([])
# 	plt.yticks([])
# 	plt.grid(False)
# 	plt.imshow(train_images[i], cmap=plt.cm.binary)
# 	plt.xlabel(class_names[train_labels[i]])
# plt.show()


#######################################
# Build the model
#######################################

# Set up the layers
model = keras.Sequential([
	keras.layers.Flatten(input_shape=(28, 28)),
	keras.layers.Dense(128, activation='relu'),
	keras.layers.Dense(10)
])

# Compile the model
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

# Display the model's architecture
model.summary()


#######################################
# Train the model
#######################################

# Feed the model
model.fit(train_images, train_labels, epochs=20)

# Evaluate accuracy
test_loss, test_accuracy = model.evaluate(test_images, test_labels, verbose=2)
test_accuracy = round(test_accuracy*100, 2)
print("\nModel accuracy on evaluation data : {}%".format(test_accuracy))

# Make predictions
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)*100
i = 0
print("\nPrediction for {} : {} ({})".format(class_names[test_labels[i]], class_names[np.argmax(predictions[i])], predictions[i]))

# afficher la prediction
plt.figure()
plt.imshow(train_images[i])
plt.colorbar()
# plt.show()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
plt.bar(class_names,predictions[i])
plt.show()
