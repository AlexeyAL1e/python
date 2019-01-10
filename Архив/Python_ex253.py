class Shape:
    def __init__(self, width, length):
        self.width = width    # ширина
        self.length = length  # длина

    def print_size(self):
        print('{} на {}'.format(self.width, self.length))


class Square(Shape):
    pass


a_square = Square(20, 20)
a_square.print_size()
