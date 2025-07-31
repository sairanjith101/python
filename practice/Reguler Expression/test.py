import re

text1 = '#$%aaabbbccc@gmail.com'
regex = r'([\w]+)@([\w]+)\.([\w]+)'

match = re.findall(regex, text1)

for number in match:
    print(number)