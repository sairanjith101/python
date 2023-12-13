from functools import reduce

# Assuming parser_all is a list of numbers
parser_all = [1, 2, 3, 4, 5]

# Using reduce to sum up the elements in parser_all
result = reduce(lambda x, y: x + y, parser_all)

print(result)