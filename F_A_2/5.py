arr = [1, 2, 'a', 'b', '3', 'c', '4', 'd', 5]

output = []

for a in arr:
    if type(a) == int:
        output.append(a)

print(output)