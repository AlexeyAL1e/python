class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return (self.base / 2) * self.height


triangle1 = Triangle(10, 7)
i = triangle1.area()
print('Площадь треугольника равна: {}'.format(i))
