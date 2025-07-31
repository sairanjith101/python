| Operation               | Command                              |
| ----------------------- | ------------------------------------ |
| **Read CSV**            | `pd.read_csv('file.csv')`            |
| **Write CSV**           | `df.to_csv('file.csv', index=False)` |
| **Head & Tail**         | `df.head()`, `df.tail()`             |
| **Summary**             | `df.info()`, `df.describe()`         |
| **Select Column**       | `df['col']`                          |
| **Filter Rows**         | `df[df['col'] > value]`              |
| **Sort**                | `df.sort_values('col')`              |
| **Group By**            | `df.groupby('col')['col2'].mean()`   |
| **Merge DataFrames**    | `pd.merge(df1, df2, on='col')`       |
| **Drop Duplicates**     | `df.drop_duplicates()`               |
| **Handle Missing Data** | `df.fillna(value)`                   |
