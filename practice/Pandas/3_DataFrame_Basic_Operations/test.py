import pandas as pd

df = pd.read_csv('data.csv')

# Append new row
df = df._append({'Name': 'Sam', 'Age': 50, 'Department': 'Claim'}, ignore_index=True)

# Drop the row with index 5
df = df.drop(index=5)

print(df)
