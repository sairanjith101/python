def swaplist(newlist):
    size = len(newlist)
    swap = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1] = swap
    return newlist
newlist = [12, 35, 9, 56, 24]
newlist_1 = [1,2,3]
print(swaplist(newlist))
print(swaplist(newlist_1))