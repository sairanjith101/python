import numpy as np

arr = [
 [1,2,3,4],
 [5,6,7,8],
 [1,2,3,4],
 [5,6,7,8]
]

output = []

for i in range(len(arr)):
    for j in range(len(arr)):
        x = [arr[j][i]]
        output.append(x)

print(np.array(output).reshape(4,4))

# arr = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ]

# output = []

# for i in range(len(arr[0])):  
#     row = []
#     for j in range(len(arr)):  
#         row.append(arr[j][i])
#     output.append(row)

# print(output)
