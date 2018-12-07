import shape_detect1 as detector 
import preprocess as pp
import os
import cv2

white = cv2.imread('white.jpg')
white = cv2.resize(white, (1800,1800))

counter = 0
#for i in os.listdir("dataset"):
#	counter+=1

img = cv2.imread('demo_template/5.png', 0)
img = pp.processImg(img)
#cv2.imwrite("temp.jpg", pp.processImg(img))

#img = cv2.imread("temp.jpg")
#img2 = cv2.imread('dataset/test1.jpg')

img3 = cv2.resize(img, (1800,1800))
img_contour = detector.contour(img3)

img_rect = detector.rect_to_cut(img_contour)

detector.cut_predict(img3,img_rect,5,white, "demo_after_cut")


#img_processed = detector.preprocess(img3)
#img2_processed = detector.preprocess(img2)

#temp = cv2.resize(img_processed, (0,0), fx=0.3, fy=0.3) 
#temp2 = cv2.resize(img2_processed, (0,0), fx=0.3, fy=0.3) 
#cv2.imshow("ucla", temp)
#cv2.imshow("old", temp2)
#cv2.waitKey(3000)

#img_contour = detector.contour(img3)
#img2_contour = detector.contour(img2_processed)

#img_rect = detector.rect_to_cut(img_contour)
#img2_rect = detector.rect_to_cut(img2_contour)

#detector.cut_predict(img,img_rect,1,white)

#for i in range (300,310):
#	img = cv2.imread('dataset/'+str(i)+'.png')
#	img3 = cv2.resize(img, (1800,1800))
#	img_contour = detector.contour(img3)
#	img_rect = detector.rect_to_cut(img_contour)
#	detector.cut_predict(img3,img_rect,i,white)
