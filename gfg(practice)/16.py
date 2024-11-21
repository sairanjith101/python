input = [12, 35, 9, 56, 24]
# input = [1,2,3]

temp = input[0]
input[0] = input[-1]
input[-1] = temp

print(input)