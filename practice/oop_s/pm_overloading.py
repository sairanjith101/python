class square:

    side = 5
    def cal_area_sq(self):
        return self.side * self.side

class triangle:

    base = 5
    height = 4
    def cal_area_tri(self):
        return 0.5 * self.base * self.height

obj_sq = square()
obj_tri = triangle()

print('Area of Square = ', obj_sq.cal_area_sq())
print('Area of Triangle = ', obj_tri.cal_area_tri())