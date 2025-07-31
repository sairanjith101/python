#class = VIR
#variable = RS mobility app
#instance variable = car
#methonds = approve, reassign, rejection

class VIR:

    portal = 'RS Mobility app'

    def __init__(self,car):
        self.maruti = car

    def status(self,approval,reassign,rejection):
        self.direct = approval
        self.first_option = reassign
        self.second_option = rejection
        print(approval,reassign,rejection)


model = VIR('swift')
print(model.portal)
print(model.maruti)
model.status('two_min','four_min','six_min')