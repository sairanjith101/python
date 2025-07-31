class goa:
    name = ""
    drink = ""

    def beach(self):
        return "Lets Go Beach"
    
    def party(self):
        return "Lets Go Party"
    

ramesh = goa()
suresh = goa()

# access class atribute
ramesh.name = "Ramesh"
print("I am : ", ramesh.name)
suresh.name = "Suresh"
print("I am : ", suresh.name)

# access clss atribute
ramesh.drink = "Yes"
print("Is Ramesh drink : ", ramesh.drink)
suresh.drink = "No"
print("Is Suresh drink : ", suresh.drink)

# access instance varible
print(ramesh.party())
print(suresh.beach())