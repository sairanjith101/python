from collections import UserList

class mylist(UserList):
    def remove(self):
        raise RuntimeError("Deletion not allowed")
    
    def pop(self):
        raise RuntimeError("Deletion not allowed")
    
l = mylist([1,2,3])
l.remove()