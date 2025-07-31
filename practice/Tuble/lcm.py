def lcm(x,y):
    if x > y:
        z = x
    else:
        z = y
    while True:
        if ((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1
    return lcm
x = int(input("Enter the 'x' value : "))
y = int(input("Enter the 'y' value : "))

print("The L.C.M is : ", lcm(x,y))


        