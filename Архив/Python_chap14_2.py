class Square:
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

    def __repr__(self):
        return '{} на {} на {} на {}'.format(self.side, self.side, self.side, self.side)


s1 = Square(10)
s2 = Square(20)
s3 = Square(5)

print(s1)
