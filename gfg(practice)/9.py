user = input("Enter a input: ")

for i in user:
    if i.isdigit():
        output = user.replace(i, '')
        break

reverse_output = output[::-1]
print(reverse_output)


    
    