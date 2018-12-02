import os
import glob
import time
import numpy as np
import tensorflow as tf
from skimage import io, transform

os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'

model_path = "./model"
if not os.path.exists(model_path): 
	os.makedirs(model_path)

def read_img(list_dir, w, h):
	fpaths = []
	imgs = []
	labels = []

	for d in list_dir: 
		for fname in os.listdir(d):
			fpath = os.path.join(d, fname)
			fpaths.append(fpath)
		
			img = io.imread(fpath)
			img = transform.resize(img, (w, h))

			index = int(fname.split("_")[0])
			
			imgs.append(img)
			labels.append(index)
	return np.asarray(imgs,np.float32), np.asarray(labels,np.float32)
	

def messOrder(data, labels): 
	num_example = data.shape[0]
	arr = np.arange(num_example)
	np.random.shuffle(arr)
	data = data[arr]
	labels = labels[arr]

	return data, labels

def segmentation(data, label, ratio=0.8):
	num_example = data.shape[0]
	s = np.int(num_example * ratio)

	x_train = data[:s]
	y_train = label[:s]
	
	x_val = data[s:]
	y_val = label[s:]

	return x_train, y_train, x_val, y_val

path = ["../data/training/paragraph","../data/training/h1","../data/training/h2","../data/training/h3","../data/training/image","../data/training/button","../data/training/garbage", "../data/testing/paragraph","../data/testing/h1","../data/testing/h2","../data/testing/h3","../data/testing/image","../data/testing/garbage"]

print("read the image")
imgs, labels = read_img(path,100,100)
print("mess up the order of the image")
imgsNew, labelsNew = messOrder(imgs, labels)
print("divide the training and testing")
x_train, y_train, x_val, y_val = segmentation(imgsNew, labelsNew, 0.8)
print("finish data processing")

def buildCNN(w, h, c):

	x = tf.placeholder(tf.float32, shape=[None, w, h, c], name='x')
	y_ = tf.placeholder(tf.int32, shape=[None, ], name='y_')


	conv1 = tf.layers.conv2d(
		inputs=x,
		filters=32,
		kernel_size=[5, 5],
		padding="same",
		activation=tf.nn.relu,
		kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
	pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)


	conv2 = tf.layers.conv2d(
		inputs=pool1,
		filters=64,
		kernel_size=[5, 5],
		padding="same",
		activation=tf.nn.relu,
		kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
	pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)


	conv3 = tf.layers.conv2d(
		inputs=pool2,
		filters=128,
		kernel_size=[3, 3],
		padding="same",
		activation=tf.nn.relu,
		kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
	pool3 = tf.layers.max_pooling2d(inputs=conv3, pool_size=[2, 2], strides=2)


	conv4 = tf.layers.conv2d(
		inputs=pool3,
		filters=128,
		kernel_size=[3, 3],
		padding="same",
		activation=tf.nn.relu,
		kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
	pool4 = tf.layers.max_pooling2d(inputs=conv4, pool_size=[2, 2], strides=2)

	re1 = tf.reshape(pool4, [-1, 6 * 6 * 128])


	dense1 = tf.layers.dense(inputs=re1,
							 units=1024,
							 activation=tf.nn.relu,
							 kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
							 kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))
	dense2 = tf.layers.dense(inputs=dense1,
							 units=512,
							 activation=tf.nn.relu,
							 kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
							 kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))
	logits = tf.layers.dense(inputs=dense2,
							 units=20,  
							 activation=None,
							 kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
							 kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))

	return logits, x, y_

def accCNN(logits, y_):
	loss = tf.losses.sparse_softmax_cross_entropy(labels=y_, logits=logits)
	train_op = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)
	correct_prediction = tf.equal(tf.cast(tf.argmax(logits, 1), tf.int32), y_)
	acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

	return loss, train_op, correct_prediction, acc

def minibatches(inputs=None, targets=None, batch_size=None, shuffle=False):
	assert len(inputs) == len(targets)
	if shuffle:
		indices = np.arange(len(inputs))
		np.random.shuffle(indices)
	for start_idx in range(0, len(inputs) - batch_size + 1, batch_size):
		if shuffle:
			excerpt = indices[start_idx:start_idx + batch_size]
		else:
			excerpt = slice(start_idx, start_idx + batch_size)
		yield inputs[excerpt], targets[excerpt]

def read_test(fpath): 
	img = io.imread(fpath)
	img = transform.resize(img, (100, 100))
	imgs = []
	imgs.append(img)
	return np.asarray(imgs,np.float32)

#def predict(fpath):
#	x_predict = read_test(fpath)
#	y_predict = tf.cast(tf.argmax(logits, 1), tf.int32) 
#	return y_predict

logits, x, y_ = buildCNN(100,100,3)
loss, train_op, correct_prediction, acc = accCNN(logits, y_)

sess=tf.InteractiveSession()  
sess.run(tf.global_variables_initializer())

is_train = False
saver = tf.train.Saver(max_to_keep=1, save_relative_paths=True)

n_epoch = 50
batch_size = 64 

if is_train: 
	for epoch in range(n_epoch):
		# training
		print("####################Epoch#########################", epoch)
		train_loss, train_acc, n_batch = 0, 0, 0
		for x_train_a, y_train_a in minibatches(x_train, y_train, batch_size, shuffle=True):
			_, err, ac = sess.run([train_op, loss, acc], feed_dict={x: x_train_a, y_: y_train_a})
			train_loss += err
			train_acc += ac
			n_batch += 1
		print("train loss: %f" % (train_loss / n_batch))
		print("train acc: %f" % (train_acc / n_batch))
		save_path = saver.save(sess,"./model",global_step=epoch+1) 
		print(save_path)
else: 
	model_file=tf.train.latest_checkpoint(".")
	saver.restore(sess,model_file)

	graph = tf.get_default_graph() 
	x = graph.get_tensor_by_name("x:0")

	data = read_test("5_0.png")
	feed_dict = {x:data}
	#logits = graph.get_tensor_by_name("logits_eval:0")

	classification_result = sess.run(logits,feed_dict)
	print(tf.argmax(classification_result,1).eval())

	
	#print("After the restoring")
	#val_loss,val_acc=sess.run([loss,acc], feed_dict={x: mnist.test.images, y_: mnist.test.labels})
	#print('val_loss:%f, val_acc:%f'%(val_loss,val_acc))
sess.close()





