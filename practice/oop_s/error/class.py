# Ramesh & suresh go to GOA

class goa:

    # class atribute
    name = ""
    dirnk = ""

    # instance variable
    def party(self):
        return "Let go party"
    
    # Normal method
    def beach(self):
        return "Lets go Beach"
    
ramesh = goa()
suresh = goa()

# access class atribute
# name
ramesh.name = "Ramesh"
suresh.name = "Suresh"
print(ramesh.name)
print(suresh.name)
# drink
ramesh.dirnk = "Yes"
suresh.dirnk = "No"
print(ramesh.dirnk)
print(suresh.dirnk)

# instance varibale access
print(ramesh.party())
print(suresh.beach())
