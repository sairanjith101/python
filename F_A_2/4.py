import re

text = "Hello Gary Williams"

regex = r'(\w+)\s(\w+)\s(\w+)'

match = re.finditer(regex, text)

for m in match:
    print("The First Name is : ", m.group(2))
    print("The Second Name is : ", m.group(3))