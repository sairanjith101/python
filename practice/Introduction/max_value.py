def krishna(a,b):
    if a > b:
        return a
    else:
        return b

a = 100
b = 200
print(krishna(a,b))
print(a if a > b else b)