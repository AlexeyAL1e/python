import math


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * (self.radius ** 2)


circle1 = Circle(3)
i = circle1.area()
print('Площадь равна: {}'.format(i))
