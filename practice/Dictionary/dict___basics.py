#Dict model 1
name = {}
name['Ranjith'] = 26
name['Kumar'] = 27
name['SK'] = 29
print(name)

#model 2
name1 = {'Ranjith' : 26, 'Kumar' : 27, 'SK' : 29}
print(name1)
#model 3
name2 = {
    'Ranjith' : 26,
    'Kumar' : 27,
    'SK' : 29
}
print(name2)

##########################################################
name2['Ranjith'] = 29
print(name2)
print(name2['SK'])
#print(name2['vijay'])
print(name2.get('vijay'))

###########################################################

#if statement
print('Kumar' in name2)

#1
if 'vijay' in name2: print(name2['vijay'])
else: print('No key')
#2
if 'vijay' in name2:
    print(name2['vijay'])
else:
    print('No key')

###########################################################

#for loop
#keys
for key in name2: print(key)

for key in name2.keys(): print(key)
print(name2.keys())

#2values
for value in name2.values(): print(value)
print(name2.values())

#3 keys, values
for key, value in name2.items(): print(key + ' ' + '==>' + ' ' + str(value))
print(name2.items())

#4 sorted
for key in sorted(name2.keys()): print(key)