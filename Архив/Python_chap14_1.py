class Square:
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)


s1 = Square(10)
s2 = Square(20)
s3 = Square(5)

print(Square.square_list)
