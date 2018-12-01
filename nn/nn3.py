# load the dataSet
# encoding:utf-8
# Python2 兼容
from __future__ import print_function, division
from scipy.io import loadmat as load
import numpy as np

def reformat(samples, labels):
    # 改变原始数据的形状
    samples = np.transpose(samples, (3, 0, 1, 2)).astype(np.float32)
    # labels 变成 one-hot
    labels = np.array([x[0] for x in labels])
    one_hot_labels = []
    for num in labels:
        one_hot = [0.0]*5
        one_hot[num] = 1.0
        one_hot_labels.append(one_hot)
    labels = np.array(one_hot_labels).astype(np.float32)
    return samples, labels

def normalize(samples):
    # 将图片从 0～255 线性映射到 -1.0～+1.0
    return (samples*1.0)/128.0 - 1.0

# load the dataset
# 用matlab制作的数据集文件  .mat文件
train = load('trainSet.mat')

print('Train Samples Shape: ', train['trainImage'].shape)
print('Train  Labels Shape: ', train['trainLabel'].shape)
_train_samples = train['trainImage']
_train_labels = train['trainLabel']

n_train_samples, _train_labels = reformat(_train_samples, _train_labels)
# normalize the images data
_train_samples = normalize(n_train_samples)

# training data
train_samples = _train_samples[0:1200]
train_labels = _train_labels[0:1200]
# test dataset
test_samples = _train_samples[1200:1500]
test_labels = _train_labels[1200:1500]

num_labels = 5
image_size = 200
num_channels = 1


if __name__ == '__main__':
    pass