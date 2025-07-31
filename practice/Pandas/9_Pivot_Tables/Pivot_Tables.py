import pandas as pd

df = pd.read_csv('data.csv')

df_pivot = pd.pivot_table(df, values='Salary', index='Age', aggfunc='mean')

print(df_pivot)