class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        if value <= 0:
            raise("Value must be Positive")
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        if value <= 0:
            raise("Value must be Positive")
        self._height = value

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)

    def __str__(self):
        return (f"Rectangle(width={self._width}, height={self._height})")
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length,side_length)

    @Rectangle.width.setter
    def width(self, value):
        self._width = value
        self._height = value
    
    @Rectangle.height.setter
    def height(self, value):
        self._height = value
        self._width = value

    def __str__(self):
        return (f"Square(side_length={self.width})")

rect = Rectangle(10,7)
print(rect)
print(f"Rectangle Area: {rect.area()}")
print(f"Rectangle Perimeter: {rect.perimeter()}")

square = Square(4)
print(square)
print(f"Square Area: {square.area()}")
print(f"Square Perimeter: {square.perimeter()}")
