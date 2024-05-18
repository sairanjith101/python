# Part I

# Define the multi-dimensional array
arr = [
    [1, 2, 3, 5],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# Initialize the sum
total_sum = 0

# Iterate over the indices and sum the elements
for i in range(len(arr)):
    total_sum += arr[i][i]

# Print the result
print("The sum of the elements is:", total_sum)

# Part II

# Define the multi-dimensional array
arr = [
    [1, 2, 3, 5],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# List of indices of the elements to sum
indices = [(0, 3), (1, 2), (2, 1), (3, 0)]

# Initialize the sum
total_sum = 0

# Iterate over the indices and sum the elements
for i, j in indices:
    total_sum += arr[i][j]

# Print the result
print("The sum of the elements is:", total_sum)


    
    


# j = 0

# for i in range(len(arr)-1,-1,-1):
#     output = output+arr[j][i]
#     j=j+1
# print(output)    