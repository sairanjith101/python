a = 'ABC'
b = 'XYZ'
c = 'ABCXYZ'

output_1 = []

for i in range(1, 50+1):
    if (i % 3 == 0) and (i % 5 == 0):
        output_1.append(c)
    elif i % 3 == 0:
        output_1.append(a)
    elif i % 5 == 0:
        output_1.append(b)
    else:
        output_1.append(i)


print(output_1)