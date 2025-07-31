# Function to find the smallest missing positive number from an unsorted array
def findsmallestmissing(nums):
    # initialize the set from array elements
    distinct = {*nums}

    # return first smallest missing positive number from the set
    index = 1
    while True:
        if index not in distinct:
            return index
        index += 1

if __name__ == "__main__":

    nums = [-1,1,2,3,0,-2,7,8]
    print('The smallest missing positive number from the array is',
        findsmallestmissing(nums))

#######################################################################

def findsmallestmissing(nums):

    distinct = {*nums}

    index = 1
    while True:
        if index not in distinct:
            return index
        index +=1

if __name__ == "__main__":

    nums = [10,20,1,2]
    print('The smallest missing positive number from the array is',
        findsmallestmissing(nums))

#########################################################################

def findsmallestmissing(nums):

    distinct = {*nums}

    index = 1
    while True:
        if index not in distinct:
            return index
        index += 1

if __name__ == '__main__':
    nums = [-5,0,2,10]
    print('The smallest missing positive number from the array is',
        findsmallestmissing(nums))