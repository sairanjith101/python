from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

s = square(5)
print(s.area())
