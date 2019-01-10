class Apple:
    def __init__(self, w, c, m, v):
        self.width = w
        self.color = c
        self.made_country = m
        self.variety = v


apple1 = Apple(700, 'красный', 'Новая зеландия', 'Гала')

print(apple1.width)
print(apple1.color)
print(apple1.made_country)
print(apple1.variety)
