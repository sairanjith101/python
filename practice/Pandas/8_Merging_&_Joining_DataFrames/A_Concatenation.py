import pandas as pd

df1 = pd.DataFrame({'A':[1,2], 'B':[3,4]})
df2 = pd.DataFrame({'C':[5,6], 'D':[7,8]})

df_conc = pd.concat([df1,df2], axis=0)

print(df_conc)

# axis=0 (default) → Concatenation happens row-wise (vertically).
# axis=1 → Concatenation happens column-wise (horizontally).