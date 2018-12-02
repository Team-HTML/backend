import tensorflow as tf 
import os 

model_path = "./model"
if not os.path.exists(model_path): 
    os.makedirs(model_path)

saver = tf.train.Saver() 
#saver.restore(sess, model_path)
