
#Dongyao Zhu

from HTML import HTML
from Tag import Tag
from Betty import shape_detect1 as detector
import myDetect
import numpy as np

def toHTML(pic):

	img = detector.readImg(pic)
	#img_processed = detector.preprocess(img)
	img_contour = detector.contour(img) #blank or img_processed
	img_rect = detector.rect_to_cut(img_contour)
	white = np.zeros((1800, 1800, 1), np.uint8)
	raw = myDetect.ml_cut_predict(img, img_rect, 1)

	html = HTML(raw)
	return html.toHTML()

f = open("test.html", 'w')
f.write(toHTML("test.png"))

