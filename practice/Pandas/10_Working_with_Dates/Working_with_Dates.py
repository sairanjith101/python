import pandas as pd

# Read the CSV file
df = pd.read_csv('data.csv')

# Add a new 'Date' column with sample values (with time included)
df['Date'] = ['2024-01-10 14:30:00', '2024-02-15 08:45:00', '2024-03-20 19:00:00', '2024-04-25 10:15:00', '2024-05-30 22:50:00']


df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.date

print(df)
