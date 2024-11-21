class parant:
    def __init__(self):
        self.h = "Mohan House"
        self.__c = "Mohan Signature"

    def signature(self):
        return self.c
    
class child(parant):
    def __init__(self):
        
        parant.__init__(self)
        print("My Father Signature")
        print(self.c)

obj_parant = parant()
print(obj_parant.h)
obj_parant.signature()
obj_child = child()
print(obj_child.)

