class student_data:
    collage = 'M A R C E T'
    location = 'Viralimalai'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def studentpercentage(self, percentage):
        print("This student has got " + str(percentage) + "% of marks in UG")

def main():
    student1 = student_data("Ranjith", 26)
    print(student1.name)
    print(student1.age)
    print(student1.collage)
    print(student1.location)
    student1.studentpercentage(90)
if __name__ == "__main__":
    main()


