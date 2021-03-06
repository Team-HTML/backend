import sys
import cv2
import numpy as np
import os
import base64

def format_path(path):
    if(path[-1:] == '/'):
        path = path[:-1]
    return path

def extension(picname):
    ind = picname.index('.')
    ext = picname[ind + 1 : ]
    return ext

def processImg(img):        
    resized = cv2.resize(img, (720,720))
    blurred = cv2.medianBlur(resized, 5)
    threshed = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,int(len(img)/20)*2-1,11)
    backtorgb = cv2.cvtColor(threshed,cv2.COLOR_GRAY2BGR)
    return backtorgb

def preprocess(path, path_to_save):
    path = format_path(path)
    path_to_save = format_path(path_to_save)
    if not os.path.exists(path_to_save):
        os.makedirs(path_to_save)
    pic_names = os.listdir(path)
    pics = ['{}/{}'.format(path,pic_name) for pic_name in pic_names]
    for i in pics:
        print(i)
    for pic,pic_name in zip(pics,pic_names):
        print(pic_name)
        img = cv2.imread(pic, 0)
        #print(img)
        threshed = processImg(img)
        ind = pic_name.index('.')
        #print(ind)
        name = path_to_save+'/'+pic_name[:ind]+'.png'
        cv2.imwrite(name, threshed)

def preprocessBlob(blob):
    img = base64.b64decode(blob)
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshed = processImg(greyed)
    return threshed
        
#if(__name__ == '__main__'):
#    path = sys.argv[1]
#    path_to_save = sys.argv[2]
#    preprocess(path, path_to_save)
