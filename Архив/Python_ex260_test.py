class Rectangle:
    recs = []

    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.recs.append(self.width)
        self.recs.append(self.length)

    def print_size(self):
        print('{} на {}'.format(self.width, self.length))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)
