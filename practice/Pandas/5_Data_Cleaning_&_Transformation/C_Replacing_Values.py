import pandas as pd

df = pd.read_csv('data.csv')

df['Name'] = df['Name'].replace('John Doe', 'John Son')
print(df)