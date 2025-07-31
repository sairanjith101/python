def Ranjith(a,b,c,d):
    if (a > b) and (a > c) and (a > d):
        Dell = a
    elif (b > a) and (b > c) and (b > d):
        Dell = b
    elif (c > a) and (c > b) and (c > d):
        Dell = c
    else:
        Dell = d
    return Dell

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
d = int(input("Enter the value of d : "))
print(Ranjith(a,b,c,d))