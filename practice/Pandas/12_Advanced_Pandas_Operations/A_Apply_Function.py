import pandas as pd

df = pd.read_csv('data.csv')

df['Salary'] = df['Salary'].apply(lambda x: x * 1.1)

print(df)