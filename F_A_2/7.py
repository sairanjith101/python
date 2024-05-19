arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

column_1 = 0
column_2 = 1
column_3 = 0
column_4 = 1


for column in arr:
    column_1 += column[0]
    column_2  *= column[1]
    column_3 += column[2]
    column_4 *= column[3]

print("The Sum of Column 1 is: ", column_1)
print("The Multiple of Column 2 is: ", column_2)
print("The Sum of Column 3 is: ", column_3)
print("The Multiple of Column 4 is: ", column_4)