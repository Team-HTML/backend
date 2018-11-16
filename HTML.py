
#Dongyao Zhu

from Tag import Tag
from heapq import heappush, heappop, heapify

class HTML():

	def __init__(self, width, height, raw):
		self.header = ('<!DOCTYPE html>\n<html>\n'
			'<head>\n\t<meta name = \"viewport\" content = \"'
			'width = device-width, initial-scale = 1, '
			'maximum-scale = 1.0, user-scalable = 0\"/>\n\t'
			'<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"/>')
		self.root = Tag(0, 0, width, height, 'body', \
			'\tbackground-color: #293030;\n')
		self.last = 0
		self.makeTree(raw)
		self.final = ''

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
	def toHTML(self, htmlPath):
		self.final += self.header + '\n<style>\n'
		self.final += 'body{\n' + self.root.style + \
			'\twidth: ' + str(self.root.W) + 'vw;\n\theight: ' + \
			str(self.root.H) + 'vw;\n}\n'
		htmlBody, inlineCSS, tab = [], [], '\t'
		#dfs
		for t in self.root.children:
			HTML.helper(htmlBody, inlineCSS, t, tab);
		self.final += ''.join(inlineCSS)
		self.final += '</style>\n</head>\n<body>\n'
		self.final += ''.join(htmlBody)
		self.final += ('</body>\n</html>\n')
		return self.final

	#write helper
	def helper(htmlBody, inlineCSS, t, tabs):
		htmlBody.append(tabs + t.openTag())
		if t.name == 'p':
			htmlBody.append(tabs + ('\tLorem ipsum dolor sit amet, pri nostrud'
				' scaevola at, ex agam habeo assueverit mei.\n'))
		if t.style != '':
			inlineCSS.append('#' + t.id + '{\n' + t.style + '\twidth: ' \
				+ str(t.wPct) + '%;\n\theight: ' + str(t.hPct) + '%;\n}\n')
		for sub in t.children:
			HTML.helper(htmlBody, inlineCSS, sub, tabs + '\t')
		htmlBody.append(tabs + t.closeTag())


