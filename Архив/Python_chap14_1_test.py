class Square:
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)


a_square = Square(29)
another_square = Square(93)

print(Square.square_list)
