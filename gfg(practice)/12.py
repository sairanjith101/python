names = { 3: 'Apple', 5: 'Water Melon', 10: 'Orange', 2: 'Fig' }


for keys,values in names.items():
    remove_char = values[:keys] + values[keys+1:]
    print(remove_char)