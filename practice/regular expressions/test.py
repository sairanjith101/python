import re

text5 = "Python created by Guido Van Rossum"
regex5 = r'([\w]+)'

match5 = re.finditer(regex5, text5, re.I) # finditer() returns iteratable object
print (match5)

for word in match5:
	print (word) # iterated object
	print (word.group()) # returns whole match
	print (word.span()) # provides start and end index of the match
	print (word.start()) # provides start index of the match
	print (word.end()) # provides end index of the match