rows = 5  # Change this value to adjust the number of rows

# Upper half of the pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Lower half of the pattern
for i in range(rows - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
