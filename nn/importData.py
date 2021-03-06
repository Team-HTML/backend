import tensorflow as tf 
import os

def _parse_function(filename, label): 
	image_string = tf.read_file(filename)
	image_decoded = tf.image.decode_jpeg(image_string)
	image_resized = tf.image.resize_images(image_decoded, [100, 100])
	return image_resized, label

 
def _read_pic(dir): 
	labels = [] 
	fpaths = [] 
	#datas = []

	for d in dir: 
		for fname in os.listdir(d):
			fpath = os.path.join(d, fname)
			fpaths.append(fpath)

			label = int(fname.split("_")[0])
			labels.append(label)

			#image = _parse_function(fname)
			

	return fpaths, labels

def transmit(): 
	list_dir = ["../data/training/paragraph","../data/training/h1","../data/training/h2","../data/training/h3","../data/training/image","../data/training/button","../data/training/garbage" ]
	fpaths, labels = _read_pic(list_dir)
	filenames = tf.constant(fpaths)
	labels = tf.constant(labels)
	
	dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))
	dataset = dataset.map(_parse_function)
	return dataset

