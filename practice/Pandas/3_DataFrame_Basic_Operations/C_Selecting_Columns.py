import pandas as pd

df = pd.read_csv('data.csv')

col = df['Age'] # Single Column
print(col)

mul_col = df[['Name', 'Age']] # Multiple Columns
print(mul_col)