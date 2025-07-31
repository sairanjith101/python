import pandas as pd

df = pd.read_csv('data.csv')

df['Name'] = df['Name'].str.upper()
print(df)