import shape_detect1 as detector 
import preprocess as detector1
import cv2
import numpy as np
import sys
import os
import math
from skimage.filters import threshold_sauvola


white = cv2.imread('white.jpg')
white = cv2.resize(white, (1800,1800))

counter = 0
#for i in os.listdir("dataset"):
#	counter+=1
img = cv2.imread('../DRAWINGS/1.jpg', 0)
img = detector1.processImg(img)
#cv2.imwrite("temp.jpg", pp.processImg(img))

#img = cv2.imread("temp.jpg")
#img2 = cv2.imread('dataset/test1.jpg')

img3 = cv2.resize(img, (1800,1800))
img_contour = detector.contour(img3)

img_rect = detector.rect_to_cut(img_contour)

detector.cut_predict(img3,img_rect,1,white)