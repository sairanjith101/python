import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(value=0, inplace=True)
print(df)