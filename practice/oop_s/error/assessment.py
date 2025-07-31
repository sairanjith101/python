class laptop:

    price = ""

    def processor(self, amd, intel):
        self.amd = amd
        self.intel = intel
        return amd or intel
        
    
    def ram(self, small, big):
        self.small = small
        self.big = big
        return small or big
    
hp = laptop()
dell = laptop()
lenovo = laptop()

# class atributes access
hp.price = "Rs.44000"
dell.price = "Rs.55000"
lenovo.price = "Rs.70000"
print("HP Laptop price is : ", hp.price)
print("DELL laptop price is : ", dell.price)
print("LONOVO Laptop price is : ", lenovo.price)

# Instance variable
hp.processor("Ryzen", "Core i5")
dell.processor("Athlon", "Core i7")
lenovo.processor("Ryzen Threadripper", "Core i9")

# Accessing instance variables
print("HP Processor:", hp.intel)
print("DELL Processor:", dell.amd)
print("LENOVO Processor:", lenovo.amd)

# instance variable
hp.ram("8GB", "16GB")
dell.ram("8GB", "16GB")
lenovo.ram("8GB", "16GB")

# accessing instance variable
print("HP Ram:", hp.small)
print("DELL Ram:", dell.big)
print("Lenovo Ram:", lenovo.small)
