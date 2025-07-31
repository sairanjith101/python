class parent:

    def __init__(self):
        self.h = 'madhan house'
        self.__s = 'madhan signature'

    def signature(self):
        print(self.s)

class child(parent):

    def __init__(self):
        
        parent.__init__(self)
        print('my father signature')
        print(self.__s)

obj_par = parent()
print(obj_par.h)
print(obj_par.signature)

#print(obj_par.s)

#obj_chi = child()
#print(obj_chi.s)