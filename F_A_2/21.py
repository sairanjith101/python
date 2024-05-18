f = int(input("Enter a Fahrenheit : "))
c = int(input("Enter a Celsius: "))

Fahrenheit = ((c/5)*9)+32
Celsius = ((f-32)/9)*(5)

print(f'{c} degrees Celsius is {round(Fahrenheit)} in Fahrenheit')
print(f'{f} degrees Fahrenheit is {round(Celsius)} in Celsius')
