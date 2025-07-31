import pandas as pd

df = pd.read_csv('data.csv')

df['Age'] = df['Age'].astype(int)
print(df)