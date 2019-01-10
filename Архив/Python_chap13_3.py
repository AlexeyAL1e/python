class Shape:                        # фигура
    def what_am_i(self):
        print('Я - фигура!')


class Rectangle(Shape):             # прямоугольник
    def __init__(self, width, length):
        self.width = width          # ширина
        self.length = length        # длина

    def calculate_perimeter(self):  # периметр
        return (self.width + self.length) * 2


class Square(Shape):                # квадрат
    def __init__(self, side):
        self.side = side            # сторона

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, resizing_side):
        self.side = self.side + resizing_side


r = Rectangle(1, 1)
s = Square(1)

r.what_am_i()
s.what_am_i()
