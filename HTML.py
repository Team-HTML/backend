
#Dongyao Zhu

from Tag import Tag
from heapq import heappush, heappop, heapify

class HTML():

	placeholder = ('Lorem ipsum dolor sit amet, pri nostrud '
				'scaevola at, ex agam habeo assueverit mei.')

	def __init__(self, raw):
		self.header = ('<!DOCTYPE html>\n<html>\n'
			'<head>\n\t<meta name = \"viewport\" content = \"'
			'width = device-width, initial-scale = 1, '
			'maximum-scale = 1.0, user-scalable = 0\"/>\n\t'
			'<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"/>')
		self.root = Tag(0, 0, 100, 100, 'body', \
			'\tbackground-color: #293030;\n')
		self.last = 0
		raw = [Tag(i[0], i[1], i[2], i[3], i[4]) for i in raw]
		self.makeTree(raw)
		self.final = ''

	def makeTree(self, tags):
		'''
	    builds the HTML tree structure from the tags
	    row by row, each row determined by a reference tag that 
	    starts most topleft and spans most row.
	    '''
		heapify(tags)
		while len(tags) > 0:
			reference = heappop(tags)
			row = []
			#get row
			while len(tags) > 0:
				neighbour = tags[0];
				if reference.bry <= neighbour.tly:
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

	def toHTML(self):
		#generate HTML and CSS source code from html structure tree, DFS
		self.final += self.header + '\n<style>\n'
		self.final += 'body{\n' + self.root.style + \
			'\twidth: 100vw;\n\theight: 100vw;\n}\n'
		html, css, tab = [], [], '\t'
		#dfs, will crash if using python2
		for t in self.root.children:
			HTML.helper(html, css, t, tab);
		self.final += ''.join(css)
		self.final += '</style>\n</head>\n<body>\n'
		self.final += ''.join(html)
		self.final += ('</body>\n</html>\n')
		return self.final

	def helper(html, css, t, tabs):
		#write helper
		html.append(tabs + t.openTag())
		if t.name == 'p' or t.name[0] == 'h':
			html.append('\n' + tabs + '\t' + HTML.placeholder + '\n' + tabs)
		if t.style != '':
			css.append('#' + t.id + '{\n' + t.style + '\twidth: ' \
				+ str(t.wPct) + '%;\n\theight: ' + str(t.hPct) + '%;\n}\n')
		if len(t.children) != 0:
			html.append('\n')
			for sub in t.children:
				HTML.helper(html, css, sub, tabs + '\t')
			html.append(tabs + t.closeTag())
		else:
			html.append(t.closeTag())
