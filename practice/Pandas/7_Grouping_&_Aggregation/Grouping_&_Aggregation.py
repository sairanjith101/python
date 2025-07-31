import pandas as pd

df = pd.read_csv('data.csv')

aggregation = df.groupby('Age').agg({'Salary': ['mean', 'max', 'min']})
print(aggregation)

