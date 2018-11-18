
#Dongyao Zhu

from HTML import HTML
from Tag import Tag
import myDetect as detector

import cv2

def toHTML(pic):

	img = detector.readImg(pic)
	img_processed = detector.preprocess(img)
	
	resize = cv2.resize(img_processed, (0,0), fx=2, fy=2)
	cv2.imshow('image',resize)
	cv2.waitKey(5000)
	cv2.destroyAllWindows()

	img_contour = detector.contour(img)#blank or img_processed

	img_rect = detector.rect_to_cut(img_contour, img.shape[0] * img.shape[1])
	#raw = detector.cut_predict(img_processed, img_rect, 1)
	raw = detector.ml_cut_predict(img, img_rect, 1)

	html = HTML(100, 100 * img.shape[0] / img.shape[1], raw)
	return html.toHTML()

f = open("test.html", 'w')
f.write(toHTML("test.png"))
