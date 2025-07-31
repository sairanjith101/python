try:
    with open('cheeta.txt', 'w') as file:
        file.read("hi")
except TypeError:
    print("its only writable not readable")
finally:
    print("successfull")