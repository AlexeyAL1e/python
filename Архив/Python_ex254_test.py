class Shape:
    def __init__(self, width, length):
        self.width = width    # ширина
        self.length = length  # длина

    def print_size(self):
        print('{} на {}'.format(self.width, self.length))


class Square(Shape):
    def __init__(self, height):
        self.height = height  # высота

    def area(self):
        return self.width * self.length


a_square = Square(20, 20, 10)

