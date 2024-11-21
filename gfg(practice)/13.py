text = 'Gavs Technologies'

user_char = input("Enter Char: ")
user_index = int(input("Enter Index: "))

new_text = text[:user_index] + user_char + text[user_index+1:]
print(new_text)
