import pandas as pd

df1 = pd.DataFrame({'ID':[1,2,3], 'NAME':['Ajith', 'Vijay', 'Dhanush']})
df2 = pd.DataFrame({'ID':[1,2,3], 'SALARY':['1000', '2000', '3000']})

df_merg = pd.merge(df1,df2, on='ID', how='inner')

print(df_merg)