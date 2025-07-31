strings1 = ['HHHH', 'lll', 'Kk', 'Gg', 's', 'A']
strings2 = ['s','A']

print(sorted(strings1))
print(sorted(strings1,key=len))
print(sorted(strings2,key=len))
print(sorted(strings1, key=str.lower))

def myfun(value):
    return value[-1]

strings3 = ['zc','ya','xe','ub']
print(sorted(strings3, key=myfun))