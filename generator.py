
#Dongyao Zhu

from HTML import HTML
from Tag import Tag

'''
    description: aligns coordinates close to each other together
    inputs: 
        errorToleranceLevel: default = 0.05, from 0 to 1
            difference of 2 coordinates on a same axis
            that could be tolerated, in percentage wrt to axis length.
        adjustLevel: default = 1, from 0 to 1
            how much to adjust each box by the average difference
'''
def align(raw, errorToleranceLevel, adjustLevel):
	allAxes = [[], []]
	for t in raw:
		allAxes[0].append((t[0], t, 0))
		allAxes[0].append((t[2], t, 2))
		allAxes[1].append((t[1], t, 1))
		allAxes[1].append((t[3], t, 3))
	for oneAxis in allAxes:
		oneAxis.sort(key = lambda tup: tup[0])
		i = 0
		refValue, refTag, refIndex = oneAxis[i]
		close = [oneAxis[i]]
		while i + 1 < len(oneAxis):
			i += 1
			nextValue, nextTag, nextIndex = oneAxis[i]
			if abs(nextValue - refValue) / 100 > errorToleranceLevel:
				adjust(close, adjustLevel)
				refValue, refTag, refIndex = oneAxis[i]
				close = [oneAxis[i]]
			else:	
				close.append(oneAxis[i])
				if i + 1 == len(oneAxis) and len(close) > 1:
					adjust(close, adjustLevel)
				continue

'''
    description: moves boxes with close coordinates on same axis together
    input:
        adjustLevel: how much to adjust each box by the average difference
'''
def adjust(close, adjustLevel):
	avg = sum([sim[0] for sim in close]) / len(close)
	for value, t, index in close:
		t[index] += (avg - value) * adjustLevel

'''
    description: call ML functions; use that output to generate HTML for lambda
'''
def toHTML(pic, errorToleranceLevel = 0.05, adjustLevel = 1.0):
	# img = detector.readImg(pic)
	# img_processed = detector.preprocess(img)
	# img_contour = detector.contour(img_processed)#blank or img_processed
	# img_rect = detector.rect_to_cut(img_contour)
	# white = np.zeros((1800, 1800, 1), np.uint8)
	# raw = detector.cut_predict(img_processed, img_rect, 1, white)

	align(raw, errorToleranceLevel, adjustLevel)
	print('aligned:\n', raw)
	html = HTML(raw)
	return html.toHTML()

##################---test---#######################
raw = []
raw.append([10.83, 70.83, 76.25, 100, 'h2'])
raw.append([12.92, 39.58, 65.83, 70, 'img'])
raw.append([10.42, 5.83, 57.50, 38.75, 'img'])
#f = open('aligned.html', 'w')
#f.write(toHTML(1))#replace 1 with some pic
#f.close()
##################---test---#######################
