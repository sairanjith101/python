# defining class
class Student_Data:

	# class variables
	college = "Karpaga Vinayaga College of Engineering and Technology"
	location = "Madurantakam"

    # constructor method with instance variable [must have 'self' keyword as first parameter]
	def __init__(self, name, age):
		# instance variables
		self.name = name
		self.age = age

	# normal method with instance variable percentage
	def studentPercentage(self, percentage):
		print("This student has got " + str(percentage) + "% of marks in UG")

# defining method main()
def main():
	
	# first object, setting up instance variables of constructor method
	student1 = Student_Data("Devid", 23)
	
	# print out instance variable - 'name' & 'age' of first object
	print(student1.name)
	print(student1.age)
	
	# print out class variable - 'college' & 'location' of first object
	print(student1.college)
	print(student1.location)
	
	# second object, setting up instance variables of constructor method
	student2 = Student_Data("Loki", 22)
	
	# print out instance variable - 'name' & 'age' of second object
	print(student2.name)
	print(student2.age)
	
	# print out class variable - 'college' & 'location' of second object
	print(student2.college)
	print(student2.location)
	
	# passing instance variable('percentage') to method ('studentPercentage')
	student1.studentPercentage(90)
	student2.studentPercentage(80)

if __name__ == "__main__":
    main()
