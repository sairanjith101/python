# Write a Python program to swap two variables.

def swap(x,y):
    temp = x
    x = y
    y = temp
    return x,y

x = 5
y = 10

print(swap(x,y))