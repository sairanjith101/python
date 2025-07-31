import pandas as pd

# Read CSV file
df = pd.read_csv('data.csv')

# Append new row (Use `pd.concat` instead of `append` in newer pandas versions)
df = pd.concat([df, pd.DataFrame([{'Name': 'Vijay', 'Age': 59, 'Department': 'vIr'}])], ignore_index=True)

print("After Append:")
print(df)

# Drop row with index 4 (Use `inplace=True` to modify `df`)
df.drop(4, inplace=True)

print("After Drop:")
print(df)
