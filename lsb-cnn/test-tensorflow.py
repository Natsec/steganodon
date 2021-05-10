import tensorflow as tf

#tf.device("/device:GPU:1")

print(tf.reduce_sum(tf.random.normal([1000, 1000])))
