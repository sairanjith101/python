# A Series is like a column in a table.

import pandas as pd

data = [10, 20, 30, 40]

s = pd.Series(data)
print(s)

# Custom Index:

s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s)

