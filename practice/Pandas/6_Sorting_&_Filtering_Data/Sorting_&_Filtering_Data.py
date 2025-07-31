import pandas as pd

df = pd.read_csv('data.csv')

df.sort_values('Age', ascending=False, inplace=True) # Sort by Age

df_filtered = df[df['Age'] > 30] # Filter rows
print(df_filtered)