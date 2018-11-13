import cv2
import numpy as np
#import scan 
import os
import myclarifai as nn
import json

#empty canvas to display rectangles on

#image to test
#img = cv2.imread('DRAWINGS/1.PNG')
#ori = img.copy()

def preprocess(img):
  #small2 = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
  #print("THIS IS THE PIC")
  #cv2.imshow("try", small2);
  #k = cv2.waitKey(1000) # 0==wait forever
  #cv2.destroyAllWindows()
  
  #img = cv2.resize(img, (1800,1800)) # we resize all images to 600
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


  gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
  gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

  # subtract the y-gradient from the x-gradient
  gradient = cv2.subtract(gradX, gradY)
  gradient = cv2.convertScaleAbs(gradient)

  # blur and threshold the image
  #gradient = img
  blurred = cv2.blur(gradient, (9, 9))
  (_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

#thresh = cv2.resize(thresh, (0,0), fx=3, fy=3)
#white = cv2.resize(white, (0,0), fx=3, fy=3)

  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
  closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

  closed = cv2.erode(closed, None, iterations=4)
  closed = cv2.dilate(closed, None, iterations=4)

  #clos = cv2.resize(closed, (0,0), fx=0.2, fy=0.2)
  return closed

#find the contour in the image 
def contour(img):
  kernel = np.ones((5,5),np.uint8)
  erosion = cv2.erode(img,kernel,iterations = 2)
  kernel = np.ones((4,4),np.uint8)
  dilation = cv2.dilate(erosion,kernel,iterations = 2)

  edged = cv2.Canny(dilation, 30, 200)

  _, contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  return contours

def rect_to_cut(contours): 

  rects = [cv2.boundingRect(cnt) for cnt in contours]
  rects = sorted(rects,key=lambda  x:x[1],reverse=True)

  real = []
  for r1 in rects:
    x1,y1,w1,h1 = r1
    area = w1 * h1
    toAdd = True
    if area > 0:#101500:
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
        if toAdd:
            real.append(r1)
  return real 

def cut(img, real, num, path, white):
  d = 0 
  for rect in real:
    x,y,w,h = rect
    area = w * h
    if area > 101500:
      print(" " + str(x) + " " + str(y) + " " + str(w) + " " + str(h))
      cv2.rectangle(white, (x, y), (x+w, y+h), (255,0,0), 6)
      #Rect rect(x,y,w,h)
      image_cut = img.copy()
      crop_img = img[y:y+h, x:x+w]
      target = "pic" + str(num) + "_" + str(d) +".jpg"
      cv2.imwrite(os.path.join(path , target), crop_img)
      d = d + 1

def cut_predict(img, real, num, white): 
  api_key = '24ba076ce08144c3833fa0d869823293'
  d = 0 
  data = {}
  for rect in real:
    x,y,w,h = rect
    area = w * h
    if area > 101500:
      print(" " + str(x) + " " + str(y) + " " + str(w) + " " + str(h))
      cv2.rectangle(white, (x, y), (x+w, y+h), (255,0,0), 6)
      #Rect rect(x,y,w,h)
      image_cut = img.copy()
      crop_img = img[y:y+h, x:x+w]
      target = "pic" + str(num) + "_" + str(d) +".jpg"
      cv2.imwrite(target, crop_img)
      maxValue, maxId = nn.prediction(target,api_key)
      data[str(d)] = []
      data[str(d)].append({
        'x': x,
        'y':y,
        'width':w,
        'height':h,
        'kind':maxId,
      })
      d = d + 1
  with open('data.json','w') as outfile:
    json.dump(data, outfile,indent=2)

#small = cv2.resize(white, (0,0), fx=0.2, fy=0.2)
#small2 = cv2.resize(img, (0,0), fx=0.2, fy=0.2)

#cv2.imshow("lalala",small)
#cv2.imshow("Sdf", small2);
#k = cv2.waitKey(10000) # 0==wait forever

#cv2.destroyAllWindows()