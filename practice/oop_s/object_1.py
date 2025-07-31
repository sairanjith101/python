class mobile:

#class variable
    brand = 'redmi'

#instance variable
    def __init__(self,model):
        self.new_model = model

#instance method
    def msg(self):
        print('i bought a redmi {}'.format(note_8.new_model))

#object
note_8 = mobile('note_8')

#access class variable
print('note_8 is a {} {}'.format(note_8.brand,'model'))

#acess instance variable
print('i bought a redmi {}'.format(note_8.new_model))

#acess instance method
note_8.msg()