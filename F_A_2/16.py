# Input = [12, 35, 9, 56, 24]
Input = [1, 2, 3, 4]

temp = Input[0]
Input[0] = Input[-1]
Input[-1] = temp

print(Input)