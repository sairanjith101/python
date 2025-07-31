file = open('sample3.txt', 'r')
print(file)

for line in file:
    print(line, end="")
    print(file.read(5))
    #file.seek(0,0)
file.close()