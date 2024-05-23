a = []
b = []

def union_array(n,m):

    for i in range(0, n):
        c = int(input("Enter a value: "))
        a.append(c)

    for i in range(0, m):
        d = int(input("Enter b value: "))
        b.append(d)

    union_list = set(a + b)
    union_count = list(union_list)
    return len(union_count)

x = int(input("Enter a size if a: "))
y = int(input("Enter a size if b: "))
print(union_array(x,y))