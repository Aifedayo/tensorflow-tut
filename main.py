import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Initialization of Tensors
x = tf.constant(4.0)

print(x)
