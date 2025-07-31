from typing import Text


text = 'Gavs Technologies'
chr = {5: 'X'}

result = ''

for index, replacement in chr.items():
    str = text[:index] + chr[index] + text[index + 1:]

print(str)