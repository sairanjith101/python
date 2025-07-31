import pandas as pd

df = pd.read_csv('data.csv')

df['Department'] = df['Department'].astype('category')

print(df)