#father class
class father(object):

    def __init__(self,name,id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(self.name)
        print(self.id_number)

    def details(self):
        print('My Name is {}'.format(self.name))
        print('ID number is {}'.format(self.id_number))

#child class
class child(father):

    def __init__(self,name,id_number,role,salary):
        self.role = role
        self.salary = salary

        father.__init__(self,name,id_number)

    def details(self):
        print('My name is {}'.format(self.name))
        print('ID number {}'.format(self.id_number))
        print('Role name is {}'.format(self.role))
        print('Salay {}'.format(self.salary))

son = child('Siva',7456,'Claims officer',25000)

son.display()
son.details()