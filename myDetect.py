import cv2
import numpy as np
import os
#import myclarifai as nn
import json

def readImg(pic):
  img = cv2.imread(pic)
  #too big for my screen
  img = cv2.resize(img, (img.shape[0]//3, img.shape[1]//3))
  return img

def preprocess(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  #smooth a bit
  img = cv2.GaussianBlur(img,(9, 9),0)
  #smooth more, preserves edges
  img = cv2.bilateralFilter(img, 5, 25, 25)
  #AT is better when there's changing light
  processed = cv2.adaptiveThreshold(img, 255, \
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 2)
  #do a closing operation to connect dashed lines
  kernel = np.ones((4, 4),np.uint8)
  processed = cv2.dilate(processed, kernel, iterations = 1)
  processed = cv2.morphologyEx(processed, cv2.MORPH_CLOSE, kernel)

  #find only lines in processed can remove most of the remaining noises
  lines = cv2.HoughLinesP(processed, 1, np.pi / 180, 50, 60, 20, 5)
  blank = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)
  for i in range(0, len(lines)):
    l = lines[i][0]
    cv2.line(blank, (l[0], l[1]), (l[2], l[3]), 255, 3, cv2.LINE_AA)
  #close a bit
  kernel = np.ones((2, 2),np.uint8)
  # closed = cv2.dilate(blank, kernel, iterations = 1)
  closed = cv2.morphologyEx(blank, cv2.MORPH_CLOSE, kernel)
  return closed

#find the contour in the image 
def contour(img):
  _, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  return contours

def rect_to_cut(contours, imgArea): 

  rects = [cv2.boundingRect(cnt) for cnt in contours]
  real = []
  i=-1
  for r1 in rects:
    i+=1
    x1,y1,w1,h1 = r1
    area = w1 * h1
    toAdd = True
    if area > imgArea * 0.04:
      #these not really needed if we use EXTERNAL in finding contour
        for r2 in real:
            x2,y2,w2,h2 = r2
            #check the exact the same one
            if x1==x2 and y1==y2:
                toAdd = False
        for r2 in rects:
            x2,y2,w2,h2 = r2
                #check if it was contained in the other
            right_x = x2 + w2
            low_y = y2 + h2
            if x2 < x1 and x1 < right_x:
                if y2 < y1 and y1 < low_y:
                    toAdd = False
        if True or toAdd:
            real.append(r1)
  return real 

def cut_predict(img, real, num): 
  api_key = '24ba076ce08144c3833fa0d869823293'
  data = []
  d = 0
  for x,y,w,h in real:
    #predict content of each rectangle
    image_cut = img.copy()
    crop_img = img[y:y+h, x:x+w]
    target = "pic" + str(num) + "_" + str(d) +".jpg"
    cv2.imwrite(target, crop_img)
    # maxValue, maxId = nn.prediction(target,api_key)
    data.append([x, y, x + w, y + h, 'p'])
    d += 1
  return data