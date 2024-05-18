# p = int(input("Enter a amount : "))
# t = int(input("Enter a time : "))
# r = float(input("Enter a rate : "))

# ci = p*((1+(r/100))**t)

# print(round(ci))

def compoundinterest(p,r,t):
    compint = p*(1+(r/100))**t
    return compint
p = float(input("Principle amount : "))
t = float(input("Time : "))
r = float(input("Rate : "))
compint = compoundinterest(p,r,t)
print("Compound Interest : ", round(compint))