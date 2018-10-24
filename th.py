import ast

def parse(file):
    for l in open(file):
        yield ast.literal_eval(l)

tags = list(parse("tags.json"))
for tag in tags:
    print('h1' in tag)
    print('h2' in tag)
    a = (tag['h1'][0], tag['h1'][0])
    print(a)

