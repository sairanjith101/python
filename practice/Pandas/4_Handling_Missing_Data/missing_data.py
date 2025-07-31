import pandas as pd

df = pd.read_csv('data.csv')

df = df.isnull().sum() # Count missing values
# # print(df)

df = df.dropna(inplace=True) # Remove missing rows
# print(df)

df = df.fillna(value=0) # Replace NaN with 0
print(df)