
#Dongyao Zhu

from HTML import HTML
from Tag import Tag

def align(raw, tolerance, adjustment):
	'''
	description: aligns coordinates close to each other together
	inputs: 
		tolerance: default = 0.05, from 0 to 1
			difference of 2 coordinates on a same axis
			that could be tolerated, in percentage wrt to axis length.
		adjustment: default = 1, from 0 to 1
			how much to adjust each box by the average difference
	TODO:
		symmetry to sides
	'''
	allAxes = [[], []]
	for t in raw:
		allAxes[0].append((t, 0))
		allAxes[0].append((t, 2))
		allAxes[1].append((t, 1))
		allAxes[1].append((t, 3))
	for oneAxis in allAxes:
		oneAxis.sort(key = lambda tup: tup[0][tup[1]])
		i = 0
		refT, refI = oneAxis[i]
		close = [oneAxis[i]]
		while i + 1 < len(oneAxis):
			i += 1
			nextT, nextI = oneAxis[i]
			if abs(nextT[nextI] - refT[refI]) / refT[refI] > tolerance:
				adjust(close, adjustment)
				refT, refI = oneAxis[i]
				close = [oneAxis[i]]
			else:	
				close.append(oneAxis[i])
				if i + 1 == len(oneAxis) and len(close) > 1:
					adjust(close, adjustment)
				continue

def adjust(close, adjustment):
	'''
	description: moves boxes with close coordinates on same axis together
	input:
		adjustment: how much to adjust each box by the average difference
	'''
	avg = sum([sim[0][sim[1]] for sim in close]) / len(close)
	for t, index in close:
		t[index] += (avg - t[index]) * adjustment

def toHTML(pic, tolerance = 0.05, adjustment = 1.0):
	'''
	description: call ML functions; use that output to generate HTML for lambda
	'''
	# img = detector.readImg(pic)
	# img_processed = detector.preprocess(img)
	# img_contour = detector.contour(img_processed)#blank or img_processed
	# img_rect = detector.rect_to_cut(img_contour)
	# white = np.zeros((1800, 1800, 1), np.uint8)
	# raw = detector.cut_predict(img_processed, img_rect, 1, white)

	align(raw, tolerance, adjustment)
	print('aligned:\n', raw)
	html = HTML(raw)
	return html.toHTML()

##################---test---#######################
raw = []
f = open('aligned.html', 'w')
f.write(toHTML(1))#replace 1 with some pic
f.close()
##################---test---#######################
