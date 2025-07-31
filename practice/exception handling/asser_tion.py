#assertion
def scale(cm):
    assert(cm>=5), "value less than 5"
    return((cm-30)*2)+40

print(scale(30))
print(scale(36.7))
print(int(scale(36.7)))
print(scale(2))