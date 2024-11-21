def sort_using_second_array(array1, array2):
    # Combine both arrays into a list of tuples (element from array1, corresponding value from array2)
    combined = list(zip(array2, array1))
    print("Combined before sorting:", combined)
    
    # Sort the combined list based on the first element of each tuple (the values from array2)
    combined.sort()
    print("Combined after sorting:", combined)

    # Initialize an empty list to store the sorted elements from array1
    sorted_array1 = []
    
    # Use a normal for loop to append the second element of each tuple (from array1) to sorted_array1
    for item in combined:
        sorted_array1.append(item[1])
    
    return tuple(sorted_array1)

# Test case
array1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
array2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

# Call the function and print the result
result = sort_using_second_array(array1, array2)
print("Sorted array1:", result)
