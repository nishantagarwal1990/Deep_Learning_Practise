#understanding session better

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
x = 2
y = 3
op1 = tf.add(x, y)
op2 = tf.multiply(x, y)
useless = tf.multiply(x, op1)
op3 = tf.pow(op2, op1)
with tf.Session() as sess:
    op3, not_useless = sess.run([op3, useless])
    print op3
    print not_useless
