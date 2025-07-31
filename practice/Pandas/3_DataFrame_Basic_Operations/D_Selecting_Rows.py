import pandas as pd

df = pd.read_csv('data.csv')

first_row = df.iloc[0] # First row
print(first_row)

first_row_numerical = df.loc[0] # First row (if index is numerical)
print(first_row_numerical)

filter_row = df.loc[df['Age']>30] # Filtering rows
print(filter_row)