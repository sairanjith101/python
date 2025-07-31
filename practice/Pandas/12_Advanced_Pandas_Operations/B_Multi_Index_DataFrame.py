import pandas as pd

df = pd.read_csv('data.csv')

df.set_index(['Age', 'Name'], inplace=True)

print(df.loc[(30, 'Jane Smith')])