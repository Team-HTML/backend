
#Dongyao Zhu

from HTML import HTML
from Tag import Tag
import myDetect as detector

def toHTML(pic):

	img = detector.readImg(pic)
	img_processed = detector.preprocess(img)
	img_contour = detector.contour(img_processed)#blank or img_processed

	img_rect = detector.rect_to_cut(img_contour, img.shape[0] * img.shape[1])
	raw = detector.cut_predict(img_processed, img_rect, 1)

	html = HTML(100, 100 * img.shape[0] / img.shape[1], raw)
	return html.toHTML()

f = open("test.html", 'w')
f.write(toHTML("test3.jpg"))
