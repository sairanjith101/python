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

for i in range(len(arr)):
        column_1 += arr[i][0]
        column_2 *= arr[i][1]
        column_3 += arr[i][2]
        column_4 *= arr[i][3]

print("Sum of column 1: ", column_1)
print("Sum of column 2: ",column_2)
print("Sum of column 3: ",column_3)
print("Sum of column 4: ",column_4)
