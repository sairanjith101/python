import sqlite3
import pandas as pd

# Connect to the database (it will create the file if it doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create the employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT
);
''')

# Insert sample data into the employees table
cursor.execute('''
INSERT INTO employees (name, email, phone)
VALUES
('John Doe', 'john.doe@example.com', '123-456-7890'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210')
''')

# Commit the changes
conn.commit()

# Query the employees table and load it into a pandas DataFrame
df = pd.read_sql("SELECT * FROM employees", conn)

# Save the DataFrame to a new table (new_table) in the database
df.to_sql("new_table", conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("Data transferred to 'new_table' successfully!")
