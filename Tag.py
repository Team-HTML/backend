
#Dongyao Zhu

'''
(0, 0)                   X
  |---------------------->
  | top left 
  |   ____________________
  |  |                    |
  |  |                    |
  |  |                    |
  |  |____________________|
  |                   bottom right
Y v
'''

class Tag:

    #name counter
	count = {'wrap' : 0}

	#no close
	voidTags = {'img', 'input'}

	def __init__(self, tlx = 0, tly = 0, brx = 0, bry = 0, name = 'div', \
		style = '', wrap = False, a = None, b = None):

		self.tlx = tlx
		self.tly = tly
		self.brx = brx
		self.bry = bry
		self.W = brx - tlx
		self.H = bry - tly
		self.S = self.W * self.H
		self.name = name
		self.style = "\tposition: relative;\n" + style
		self.children = []
		#creates an actual Tag
		if wrap == False:
			self.name = name
			self.cls = name
			if name in Tag.count:
				Tag.count[name] += 1
				self.id = name + str(Tag.count[name])
			else:
				Tag.count[name] = 1
				self.id = name + '1'
			self.wPct = self.W
			self.hPct = self.H
			if name == 'p' or name[0] == 'h':
				self.style += "\tmargin: 0%;\n\tpadding: 1px;\n"
				self.style += "\toverflow: scroll;\n\tcolor: white;\n"
				self.style += "\tborder: 1px white dashed;\n"
		#creates a wrapper Tag
		else:
			Tag.count['wrap'] += 1
			self.cls = 'wrap'
			self.id = 'wrap' + str(Tag.count['wrap'])
			self.children.append(a)
			a.wPct = 100 * a.W / self.W
			a.hPct = 100 * a.H / self.H
			self.wPct = self.W
			self.hPct = self.H
			if(b != None):
				self.children.append(b)
				b.wPct = 100 * b.W / self.W
				b.hPct = 100 * b.H / self.H
				
	def __lt__(self, t):
		#comparison for priority queue
		return True if self.tly < t.tly else False if self.tly > t.tly \
			else True if self.H > t.H else False

	def __str__(self):
		#for debug
		return self.name + ' - '  + self.id + ' - ' + self.cls + ': ' + \
			str(self.tlx // 1) + ', ' + str(self.tly // 1) + ', ' + \
			str(self.brx // 1) + ', ' + str(self.bry // 1)

	def expandRow(self, t):
		'''
		if t protrudes downwards, this tag will be wrapped with one 
	    expanding to t's botRightY so this can include more tags as a row)
	    '''
		if(t.bry > self.bry): 
			return Tag(self.tlx, self.tly, self.brx, t.bry, \
				'div', '', True, self, None)
		return self

	def wrap(a, b):
		'''
		used to wrap 2 tags in a bigger parent tag, 
		and their positions are relative to their parent now.
		'''
		#smallest tly, tlx, largest bry, brx
		t = Tag(min(a.tlx, b.tlx), min(a.tly, b.tly), \
			max(a.brx, b.brx), max(a.bry, b.bry), 'div', '', True, a, b)
		#below are dirty css tricks
		#horizontal adjustment
		ax = 100 * (a.tlx - t.tlx) / t.W
		if ax > 0:
			a.style += '\tleft: ' + str(ax) + '%;\n'
		bx = 100 * (b.tlx - t.tlx) / t.W
		if bx > 0:
			b.style += '\tleft: ' + str(bx) + '%;\n'
		#vertical adjustment
		ay = 100 * (a.tly - t.tly) / t.H
		if ay > 0:
			a.style += '\ttop: ' + str(ay) + '%;\n'
		by = 100 * (b.tly - t.tly - a.H) / t.H
		if by != 0:
			b.style += '\ttop: ' + str(by) + '%;\n'
		return t

	def openTag(self):
		#returns opening tag to be written in html file
		t = '<' + self.name
		if self.id != '':
			t += ' id = \"' + self.id + '\"'
		if self.cls != '':
			t += ' class = \"' + self.cls + '\"'
		if self.cls == 'button':
			t += ' onclick = "alert(\'Greetings!\')"click me'
		if self.cls == 'input':
			t += ' type = "text" placeholder = "is PHP the best language?"'
		return t + '>'

	def closeTag(self):
		#returns closing tag to be written in html file
		if self.name in Tag.voidTags:
			return '\n'
		return '</' + self.name + '>\n'

