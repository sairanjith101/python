def findname(text):
    split_name = text.split()

    first_name = split_name[1]
    second_name = split_name[2]

    return first_name, second_name

text = "Hello Gary Williams"

first_name , second_name = findname(text)

print("First Name: ", first_name)
print("Second Name: ", second_name)