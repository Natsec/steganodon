# https://www.tensorflow.org/tutorials/keras/save_and_load

import os
import tensorflow as tf
from tensorflow import keras

print(tf.version.VERSION)


# modèle d'exemple
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_labels = train_labels[:1000]
test_labels = test_labels[:1000]
train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0


# Define a simple sequential model
def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10)
  ])

  model.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=[tf.metrics.SparseCategoricalAccuracy()])

  return model

# Create a basic model instance
model = create_model()
# Display the model's architecture
model.summary()


# sauvegarde de checkpoint
########################################

checkpoint_path = "training1_checkpoint/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# Train the model with the new callback
model.fit(train_images,
          train_labels,
          epochs=10,
          validation_data=(test_images, test_labels),
          callbacks=[cp_callback])  # Pass callback to training

# This may generate warnings related to saving the state of the optimizer.
# These warnings (and similar warnings throughout this notebook)
# are in place to discourage outdated usage, and can be ignored.


# restauration de checkpoint
########################################

# Create a basic model instance
new_model = create_model()

# Evaluate the model
loss, acc = new_model.evaluate(test_images, test_labels, verbose=2)
print("Untrained model, accuracy: {:5.2f}%".format(100 * acc))

# Loads the weights
new_model.load_weights(checkpoint_path)

# Re-evaluate the model
loss, acc = new_model.evaluate(test_images, test_labels, verbose=2)
print("Restored model, accuracy: {:5.2f}%".format(100 * acc))


# sauvegarde d'un model entier
# permet d'importer dans tensorflow.js
########################################

# Save the entire model as a SavedModel.
new_model.save('saved_models/my_new_model')


# restauration d'un model entier
########################################

new_model = tf.keras.models.load_model('saved_models/my_new_model')
# Check its architecture
new_model.summary()
