import pandas as pd

data  = {
    'Name': ['Sai', 'Karan', 'Vinoth', 'Sam', 'Ethan'],
    'Age': [20, 25, 30, 35, 40],
    'Salary': ['10000', '20000', '30000', '40000', '50000'],
    'Department': ['Vir', 'claim','Frontend', 'Backend', 'Database']
}

df = pd.DataFrame(data)
print(df)