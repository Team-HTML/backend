
#Dongyao Zhu

from HTML import HTML
from Tag import Tag

#raw = cut_predict(...), then pass it to html

raw = []
raw.append(Tag(10, 10, 40, 90, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(60, 10, 90, 40, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(60, 60, 70, 90, 'p', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(80, 60, 90, 90, 'p', '\tborder: 2px solid white;\n', ''))
html = HTML(100, 100, raw)
html.write('test1.html')

raw.append(Tag(20, 40, 80, 60, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(40, 10, 60, 30, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(40, 70, 60, 90, 'div', '\tborder: 2px solid white;\n', ''))
html = HTML(100, 100, raw)
html.write('test2.html')

raw.append(Tag(10, 10, 60, 40, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(40, 60, 90, 90, 'div', '\tborder: 2px solid white;\n', ''))
html = HTML(100, 100, raw)
html.write('test3.html')

raw.append(Tag(10, 10, 40, 90, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(15, 20, 20, 80, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(25, 20, 30, 80, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(60, 10, 70, 40, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(50, 20, 80, 30, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(50, 60, 60, 80, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(50, 80, 70, 90, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(70, 70, 80, 90, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(60, 60, 80, 70, 'div', '\tborder: 2px solid white;\n', ''))

html = HTML(100, 100, raw)
html.write('test4.html')

raw.append(Tag(10, 10, 15, 90, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(26, 10, 40, 90, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(60, 10, 85, 90, 'div', '\tborder: 2px solid white;\n', ''))
raw.append(Tag(90, 10, 95, 90, 'div', '\tborder: 2px solid white;\n', ''))

html = HTML(100, 100, raw)
html.write('test5.html')
