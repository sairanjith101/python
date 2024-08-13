# Write a Python program to find the square root of a number.

def sqrRoot(num):
    sqr_root = num ** 0.5
    return sqr_root

num = int(input("Enter a number: "))

print(sqrRoot(num))