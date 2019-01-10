class AlwaysPositive:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return abs(self.number)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x+y)