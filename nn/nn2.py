import tensorflow as tf
import numpy as np 
import os 
import importData

train_data_dir = "data"

train = True 
model_path = "model"

#actually evoke the function to read in data 
print("Start on the data")
dataset= importData.transmit()
print("Finish preprocessing the data of training")

print(dataset.output_shapes)
#num_classes = len(set(labels))