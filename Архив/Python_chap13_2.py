
class Rectangle:                    # прямоугольник
    def __init__(self, width, length):
        self.width = width          # ширина
        self.length = length        # длина

    def calculate_perimeter(self):  # периметр
        return (self.width + self.length) * 2


class Square:                       # квадрат
    def __init__(self, side):
        self.side = side            # сторона

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, new_side):
        self.side = self.side + new_side


r = Rectangle(3, 4)
s = Square(2)
print(r.calculate_perimeter())
print(s.calculate_perimeter())

s.change_size(-1)
print(s.calculate_perimeter())
