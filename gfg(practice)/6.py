
def finddsde(arr):
    output = 0

    for i in range(len(arr)):
        output += arr[i][i]
    
    return output

arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

print(finddsde(arr))