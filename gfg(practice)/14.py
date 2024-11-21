arr = [
 [1,2,3,4],
 [5,6,7,8],
 [1,2,3,4],
 [5,6,7,8]
]

tran_mat = []

for i in range(len(arr)):
    x = []
    for j in range(len(arr)):
        mat = arr[j][i]
        x.append(mat)
    tran_mat.append(x)

print(tran_mat)