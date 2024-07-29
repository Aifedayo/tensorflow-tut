import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
# Initialization of Tensors
x = tf.constant(4.0, shape=(1, 1), dtype=tf.float32)

# To create a matrix (2 x 3)
x = tf.constant([[1, 2, 3], [4, 5, 6]])

x = tf.ones((3, 3))

x = tf.zeros((2, 3))

x = tf.eye(2) # I for identity matrix


print(x)
