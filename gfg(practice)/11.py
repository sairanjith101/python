arr = [16, 6, 8, 4, 144]

output = []

for i in arr:
    squr_value = i ** 0.5
    squr_value = int(squr_value)
    if squr_value * squr_value == i:
        output.append(i)

print(output)