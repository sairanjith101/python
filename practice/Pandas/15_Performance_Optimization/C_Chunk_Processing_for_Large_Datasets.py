import pandas as pd

def process(chunk):
    # Example: Print first 5 rows of each chunk
    print(chunk.head())

# Read CSV in chunks of 1000 rows
for chunk in pd.read_csv("data.csv", chunksize=1000):
    process(chunk)
