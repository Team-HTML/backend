import tensorflow as tf
import numpy as np 
import os 
import read 
import PIL

train_data_dir = "data"

train = True 
model_path = "model"

#actually evoke the function to read in data 
fpaths, datas, labels = read.transmit()
print("Finish preprocessing the data of training")

num_classes = len(set(labels))