import os #read from the image 
from PIL import Image 
import numpy as np 
import tensorflow as tf 
import read 

#this is the train dataset 
train_data_dir = "data" 
#set it to be true. 
train = True 
model_path = "model"

#actually evoke the function to read in data 
fpaths, datas, labels = read.transmit()
print("Finish preprocessing the data of training")
num_classes = len(set(labels))
#define the placeholder. 
#placeholder includes the image data, label, dropout rate 
datas_placeholder = tf.placeholder(tf.float32, [None,32,32,3])
labels_placeholder = tf.placeholder(tf.int32, [None])

#the one we save for the dropput 
dropput_placeholder = tf.placeholder(tf.float32)

#the cnn part 
#20 convolution, 5 size for each layer
conv0 = tf.layers.conv2d(datas_placeholder, 20, 5, activation=tf.nn.relu) 
#this the max pooling 
pool0 = tf.layers.max_pooling2d(conv0,[2,2],[2,2])

conv1 = tf.layers.conv2d(pool0,40,4,activation=tf.nn.relu)
pool1 = tf.layers.max_pooling2d(conv1,[2,2],[2,2])

#this is the fully connected part 
flatten = tf.layers.flatten(pool1)

#this is to prevent the ourfitting
fc = tf.layers.dropout(fc, 400, dropput_placeholder)

dropout_fc = tf.layers.dropout(fc, dropput_placeholder)

#output layer 
logits = tf.layers.dense(dropout_fc, num_classes)

predicted_labels = tf.arg_max(logits,1)

#calculate the losses 
losses = tf.nn.softmax_cross_entropy_with_logits(
	labels = tf.one_hot(labels_placeholder, num_classes),
	logits=logits
)

mean_loss = tf.reduce_mean(losses)

#this is the optimizer to 
optimizer = tf.train.AdamOptimizer(learning_rate=1e-2).minimize(losses)

#this is used to save the model 
saver = tf.train.Saver() 

with tf.Session() as sess:
	#since we have a boolean variable to define if we are in the training phase or test phase 
	if train: 
		print("This is the training model")
		#initialize the parameters at first 
		sess.run(tf.global_variables_initializer())
		train_feed_dict = {
			daras_placeholder: datas, 
			labels_placeholder: labels,  
			dropput_placeholder: 0.25
		}

		for step in range(150): 
			_, mean_loss_val = sess.run([optimizer, mean_loss], feed_dict=train_feed_dict)
			if step % 10 == 0: 
				print("step ={}\t mean loss = {}".format(step,mean_loss_val))
		saver.save(sess, model_path)
		print("finish training")
	else:
		print("This is the testing model")
		saver.restore(sess, model_path)
		print("Loade the model")
		label_name_dict = {
			0: "h1", 
			1: "h2", 
			2: "h3", 
			3: "button", 
			4: "paragraph"
		}
		test_feed_dict = {
			datas_placeholder: datas, 
			labels_placeholder: labels, 
			dropput_placeholder: 0
		}

		test_feed_dict = {
			datas_placeholder: datas,
			labels_placeholder: labels, 
			dropput_placeholder: 0
		}
		
		predicted_labels_val = sess.run(predicted_labels, feed_dict = test_feed_dict)

		#compare the real labels and predicted labels 
		for fpath, real_label, predicted_label in zip(fpaths, labels, predicted_labels_val): 
			real_label_name = label_name_dict[real_label]
			predicted_label_name = label_name_dict[predicted_label]
			print("{}\t{} => {}".format(fpath,real_label_name, predicted_label_name))