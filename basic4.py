import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
a = tf.constant([2, 2], name="a")
b = tf.constant([[0, 1], [2, 3]], name="b")
x = tf.add(a, b, name="add")
y = tf.multiply(a, b, name="mul")
with tf.Session() as sess:
    x, y = sess.run([x, y]) 
    print x, y
