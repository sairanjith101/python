from collections import ChainMap

d1 = {'a':1,'b':2}
d2 = {'c':3, 'd':4}
d3 = {'e':5}

cm = ChainMap(d1,d2,d3)

d4 = {'f':6}

cm1 = cm.new_child(d4)

print(cm1)