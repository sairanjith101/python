def smp_num(arr):
    miss_num = []

    for i in range(1,max(arr)):
        if i not in arr:
            miss_num.append(i)

    return (min(miss_num))

arr = [-1, 1, 2, 3, 0, -2, 7, 8]
# arr = [10, 20, 1, 2]
# arr = [-5, 0, 2, 10]

print(smp_num(arr))