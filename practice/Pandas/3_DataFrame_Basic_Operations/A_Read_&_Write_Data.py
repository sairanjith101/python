import pandas as pd

# Read CSV File
df = pd.read_csv('data.csv')

# Write CSV File
df.to_csv('output.csv', index=False)

# Read Excel File
df = pd.read_excel('file.xlsx')