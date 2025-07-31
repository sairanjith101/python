import pandas as pd

df = pd.read_csv('data.csv')
df_filter = df[df['Age'] > 30]
print(df_filter)