from audioop import reverse


numbers1 = [6,7,4,2,9,1,3]
numbers2 = ['4','7','44','2','1','72']
alphabets = ['d','f','m','p','z']
strings = ['SSS','nnnn','Ll','gG','e']

print(sorted(numbers1))
print(sorted(numbers2))
print(sorted(alphabets))
print(sorted(strings))

print(numbers1)
numbers1.sort()
print(numbers1)
print(numbers1)

print(sorted(alphabets, reverse = True))