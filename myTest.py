import myDetect as detector 
import cv2
import numpy as np
import sys
import math
from skimage.filters import threshold_sauvola

img = cv2.imread(sys.argv[1])
#too big for my screen
img = cv2.resize(img, (img.shape[0]//3, img.shape[1]//3))
drawBox = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)

img_processed = detector.preprocess(img)
img_contour = detector.contour(img_processed)#blank or img_processed

drawCon = drawBox.copy()
cv2.drawContours(drawCon, img_contour, -1, 255)
cv2.imshow("ct", drawCon)

img_rect = detector.rect_to_cut(img_contour, img.shape[0] * img.shape[1])
detector.cut_predict(img_processed, img_rect, 1, drawBox)
cv2.imshow("db", drawBox)
cv2.waitKey()