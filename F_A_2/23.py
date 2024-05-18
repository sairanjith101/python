data_array = [1452, 11.23, None, 'True', 'w3resource', [0, -1], {'class': 'V', 'section': 'A'}]

for item in data_array:
    data_type = type(item).__name__
    print(f"{item}: {data_type}")
