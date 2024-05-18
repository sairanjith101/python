array1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
array2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

sorted_pairs = sorted(zip(array2, array1))
# print(sorted_pairs)
sorted_array1 = [pair[1] for pair in sorted_pairs]

print(tuple(sorted_array1))





      


