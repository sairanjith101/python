#user_defined_exception
class car_race(RuntimeError):
    def __init__(self,arg):
        self.out = arg
try:
    raise car_race('one car left the race')
except car_race as cr:
    print(cr.out)