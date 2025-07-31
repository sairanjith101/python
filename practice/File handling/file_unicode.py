import codecs

file = codecs.open('sample1.txt', 'r', 'utf-8')
for line in file:
	print (line) # unicode string
file.close()
