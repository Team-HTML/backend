import cv2

def preprocess(img): 

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (9, 9),0) 

	gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0)
	gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1)

	gradient = cv2.subtract(gradX, gradY)
	gradient = cv2.convertScaleAbs(gradient)

	blurred = cv2.GaussianBlur(gradient, (9, 9),0)
	(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
	
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
	closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

	closed = cv2.erode(closed, None, iterations=4)
	closed = cv2.dilate(closed, None, iterations=4)

	return closed

def contour(img): 
	(_,cnts,_) = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	return cnts

def rect(cnts): 
	rects = [cv2.boundingRect(cnt) for cnt in contours]
	rects = sorted(rects,key=lambda  x:x[1],reverse=True)
	
	

img = cv2.imread('DRAWINGS/1.jpg')

small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.imshow("Sdf", small);
k = cv2.waitKey(1000)

img1 = preprocess(img)
small2 = cv2.resize(img1, (0,0), fx=0.5, fy=0.5)
cv2.imshow("after preprocess", small2);
k = cv2.waitKey(1000)

