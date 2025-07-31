import itertools

numbers = [4,4,5,3]
target = 8

result = [seq for i in range(len(numbers), 0, -1)
        for seq in itertools.combinations(numbers, i)
        if sum(seq) == target]

print(result)

###################################################################

import itertools

numbers = [-7,1,5,1,4]
target = 6

result = [seq for i in range(len(numbers), 0, -1)
        for seq in itertools.combinations(numbers, i)
        if sum(seq) == target]

print(result)