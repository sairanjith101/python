# 6. Sum the diagonal elements(4+7+2+5) in a given multi-dimensional array.

arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

output = 0

list_indexes = [0,3],[1,2],[2,1],[3,0]

for i,j in list_indexes:
    output += arr[i][j]

print(output)