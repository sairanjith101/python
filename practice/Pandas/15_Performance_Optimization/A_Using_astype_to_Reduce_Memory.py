import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

df['Age'] = df['Age'].astype(np.int8)
print(df)