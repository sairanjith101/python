import pandas as pd

df = pd.read_csv('data.csv')

df.rename(columns={'Years':'Age'}, inplace=True)
print(df)