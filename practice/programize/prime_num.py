# A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
# 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors.
# But 6 is not prime (it is composite) since, 2 x 3 = 6.

num = int(input("Enter a number: "))

flag = False

if num == 1:
    print(f'{num} is not Prime Number')
elif num > 1:
    for i in range(2,num):
        if (num % i == 0):
            flag = True
            break

if flag:
    print(f'{num} is not a Prime Number')
else:
    print(f'{num} is Prime Number')