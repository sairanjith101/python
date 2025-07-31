import pandas as pd
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT
);
''')

cursor.execute('''
INSERT INTO  books (name, email, phone)
VALUES
('John Doe', 'john.doe@example.com', '123-456-7890'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210')
''')
conn.commit()
df = pd.read_sql('SELECT * FROM books', conn)

df.to_sql("new_table", conn, if_exists='replace', index=False)

conn.close()

print("Data transferred to 'new_table' successfully!")