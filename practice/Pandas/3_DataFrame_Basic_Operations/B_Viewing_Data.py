import pandas as pd

df = pd.read_csv('data.csv')

haed = df.head() # First 5 rows
print(haed)

tail = df.tail() # Last 5 rows
print(tail)

info = df.info() # Summary
print(info)

describe = df.describe() # Statistics
print(describe)