
def max_sum_of_contiguous(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
    # max_ending_here = max(Arr[1], (max_ending_here+Arr[1]))
    # max_so_far = max(max_so_far, max_ending_here)

        max_ending_here = max(arr[i], (max_ending_here+arr[i]))
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far
    
Arr = [1, 2, 3, -2, 5]
print(max_sum_of_contiguous(Arr))