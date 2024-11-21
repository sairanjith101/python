import re

text = "Hello Gary Williams"

regex = r'(\w+\s)(\w+\s)(\w+)'

match = re.finditer(regex, text)

for i in match:
    print("First Name: ", i.group(2))
    print("Second Name: ", i.group(3))


