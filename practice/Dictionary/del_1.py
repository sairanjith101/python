#del
count = 50
print(count)
del count
#print(count)

#
words = ['z','y','x','w','v','u']
print(words)
print(len(words))
del words[0]
print(words)
del words[-3 : -1]
print(words)
print(len(words))

#
tree = {'f' : 4, 'g' : 7, 'w' : 4, 'a' : 9}
print(tree)
print(len(tree))
del tree['w']
print(tree)
print(len(tree))
