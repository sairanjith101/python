class office:

    name = "ISSS"
    location = "Trichy"

    def __init__(self, emp_id, emp_name):
        self.id = emp_id
        self.name = emp_name

    def dept(self,dept):
        print("IT team: ", dept)

def main():

    employee_1 = office(12345,"Ranjith")
    employee_2 = office(23415, "Kumar")

    print(employee_1.id)
    print(employee_1.name)
    employee_1.dept("Python Developer")

if __name__ == "__main__":
    main()

