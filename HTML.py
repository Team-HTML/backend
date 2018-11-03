
#Dongyao Zhu

from Tag import Tag
from heapq import heappush, heappop, heapify

class HTML():

	def __init__(self, width, height, raw):
		self.header = ('<!DOCTYPE html>\n<html>\n'
			'<head>\n\t<meta name = \"viewport\" content = \"'
			'width = device-width, initial-scale = 1, '
			'maximum-scale = 1.0, user-scalable = 0\"/>\n')
		self.css = '\t<link rel=\"stylesheet\" type=\"text/css\" href=\"'
		self.moreCSS = ''
		self.root = Tag(0, 0, width, height, 'body', \
			'\tbackground-color: #293030;\n')
		self.last = 0
		self.makeTree(raw)

	'''
	builds the HTML tree structure from the tags
    row by row, each row determined by a reference tag that 
    starts most topleft and spans most row.
    '''
	def makeTree(self, tags):
		heapify(tags)
		while len(tags) > 1:
			reference = heappop(tags)
			row = []
			#get row
			while len(tags) > 0:
				neighbour = tags[0];
				if(reference.bry <= neighbour.tly):
					break
				else:
					reference = reference.expandRow(neighbour)
					heappush(row, neighbour)
					heappop(tags)
			heappush(row, reference)
			#merge row
			while len(row) > 1:
				a = heappop(row)
				b = heappop(row)
				heappush(row, Tag.wrap(a, b))
			if len(row) == 1:
				t = heappop(row)
				moveY = t.tly - self.last
				t.style += '\ttop: ' + str(moveY) + '%;\n'
				t.style += '\tleft: ' + str(t.tlx) + '%;\n'
				#total vertical adjustments
				self.last = t.bry - moveY if moveY > 0 else 0
				self.root.children.append(t)

	#generate HTML and CSS source code from html structure tree, DFS
	def write(self, htmlPath, cssPath):
		html = open(htmlPath, 'w')
		css = open(cssPath, 'w')
		html.write(self.header + self.moreCSS + self.css + cssPath + \
			'">\n</head>\n<body>\n')
		css.write('body{\n' + self.root.style + \
			'\twidth: ' + str(self.root.W) + 'vw;\n\theight: ' + \
			str(self.root.H) + 'vw;\n}\n')
		tab = '\t'
		#dfs
		for t in self.root.children:
			HTML.helper(html, css, t, tab);
		html.write('</body>\n</html>\n')
		html.close();
		css.close();

	#write helper
	def helper(html, css, t, tabs):
		html.write(tabs + t.openTag())
		if t.cls != 'wrap':
			html.write(tabs + '\t' + t.id + '\n')
		if t.style != '':
			css.write('#' + t.id + '{\n' + t.style + '\twidth: ' + str(t.wPct)
				+ '%;\n\theight: ' + str(t.hPct) + '%;\n}\n\n')
		for sub in t.children:
			HTML.helper(html, css, sub, tabs + '\t')
		html.write(tabs + t.closeTag())

	#for using multiple css files call multiple times to add more
	def addStyle(cssPath):
		moreCSS += self.css + cssPath + '\">\n'

