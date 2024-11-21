from collections import Counter

arr = {'sun', 'mon', 'tue', 'sun', 'mon', 'tue', 'mon', 'tue', 'thu'}

count_arr = Counter(arr)
print(count_arr)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~````

new_arr = {}
for a in arr:
    if a not in new_arr:
        new_arr[a] = 1
    else:
        new_arr[a] += 1

print(new_arr)