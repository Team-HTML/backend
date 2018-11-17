#this file will read in data 

import os #read from the image 

#this is the read data function to preprocess the data from the directory where we store the 
def read_data(train_data_dir): 
	datas = [] 
	labels = [] 
	fpaths = [] 
	#iterate through each of the image and add their data and label into the matrix 
	for fname in os.listdir(train_data_dir): 
		fpath = os.path.join(data_dir, fname)
		fpaths.append(fpath)
		image = Image.open(fpath)
		data = np.array(image) / 255.0 
		label = int(fname.split("_")[0])
		datas.append(data)
		labels.append(label)

	datas = np.array(datas)
	labels = np.array(labels)
	#sanity check to see the shape of the matrix 
	print("shape of the datas after the preprocessing: {}\tshape of labels: {}".format(datas.shape,labels.shape))
	return fpaths, datas, labels