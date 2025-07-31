class Car:

    brand = "Audi"
    wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def display_info(self):
        print(f'Brand: {Car.brand}')
        print(f'Model: {self.model}')
        print(f'Price: {self.price}')
        print(f'Wheel: {self.wheels}')

car1 = Car("Innova", 150000)
car2 = Car("Fortuner", 200000)

car1.display_info()
print("-----------------")
car2.display_info()