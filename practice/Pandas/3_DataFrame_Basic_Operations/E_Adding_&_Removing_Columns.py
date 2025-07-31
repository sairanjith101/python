import pandas as pd

df = pd.read_csv('data.csv')
print(df)

df['new_column'] = df['Age'] * 2 # Add Column
print(df)

df.drop('new_column', axis=1, inplace=True) # Remove Column
print(df)

