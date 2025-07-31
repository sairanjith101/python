name = "Hello Gary Williams"
first_name = name.split(' ').pop(0)
last_name = name.split(' ').pop(2)
print("First Name : ", first_name)
print("Last Name : ", last_name)

#########################################

import re

text = "Hello Gary Williams"

#regex = r'([\w]+)'
regex = r"^.*$"

match = re.findall(regex, text, re.I) # finds all the matches and returns it in list

for name in match:
    print (name)
    