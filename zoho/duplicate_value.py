def duplicate(a):
    original_arr = []
    duplicate_arr = []
    
    for i in a:
        if i not in original_arr:
            original_arr.append(i)
        elif i not in duplicate_arr:
            duplicate_arr.append(i)
        
    if len(duplicate_arr) == 0:
        return -1
    else:
        return duplicate_arr

# arr = [1,2,3]
arr = [1,2,3,2,3]
print(duplicate(arr))