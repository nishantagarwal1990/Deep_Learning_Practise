#Initial attempt at using tensorflow

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

a = tf.add(3,5)
#print a
sess = tf.Session()
print sess.run(a)
sess.close()
