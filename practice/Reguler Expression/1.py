import re

text5 = "Python created by Guido Van Rossum"
regex = r'([\w]+)'

match1 = re.finditer(regex, text5)

for name in match1:
    print(name)
    print(name.group())
    print(name.span())
    print(name.end())