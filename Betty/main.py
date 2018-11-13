import shape_detect1 as detector 
import cv2

white = cv2.imread('white.jpg')
white = cv2.resize(white, (1800,1800))

img = cv2.imread('test3.jpg')
img_processed = detector.preprocess(img)
img_contour = detector.contour(img_processed)
img_rect = detector.rect_to_cut(img_contour)
detector.cut_predict(img,img_rect,1,white)
