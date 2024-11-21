from itertools import combinations

def sumofcomb(arr):
    count = 0
    combination = combinations(arr,2)
    for comb in combination:
        if total == sum(comb):
            count += 1
    return count

# arr = [4, 4, 5, 3]
# total = 8
arr = [-7, 1, 5, 1, 4]
total = 6

print(sumofcomb(arr))