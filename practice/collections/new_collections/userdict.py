from collections import UserDict

class mydict(UserDict):
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
    
    def pop(self):
        raise RuntimeError("Deletion not allowed")
    
    def popitem(self):
        raise RuntimeError("Deletion not allowed")
    
d = mydict({
    'a': 1,
    'b': 2,
    'c': 3
})

d.pop()
