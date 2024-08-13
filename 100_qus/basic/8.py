# Write a Python program to check if a number is positive, negative, or zero.

def checkNum():
    try:
        num = int(input("Enter a number: "))
        if num > 0:
            print(f'{num} is a Positive Number')
        elif num == 0:
            print(f'{num} is zero')
        else:
            print(f'{num} is a Negative Number')
    except ValueError:
        print("This is not a valid integer. Please enter a correct integer value.")

if __name__ == "__main__":
    checkNum()