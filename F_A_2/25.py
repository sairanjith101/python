row = int(input("Enter a Row value: "))
column = int(input("Enter a Column value: "))

output = []

for i in range(0, row):
    x = []
    for j in range(0, column):
        x.append(i*j) 
    output.append(x)

print(output)


