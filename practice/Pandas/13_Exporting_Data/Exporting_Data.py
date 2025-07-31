import pandas as pd

df = pd.read_csv('data.csv')

df.to_csv('output.csv')

df.to_excel('output.xlsx')

df.to_json('output.json')