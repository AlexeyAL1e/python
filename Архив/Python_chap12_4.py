
# Copyright (C) 2018 #Popov Andrei.
# Licensed to the Python Software Foundation under a contributor agreement.
# See LICENSE.txt and CONTRIBUTORS.txt.


class Hexagon(object):
    """
    This class create an object hexagon with side equally s
    """
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 6 * self.side


hex1 = Hexagon(10)
i = hex1.calculate_perimeter()
print('Периметр Hexagon равен: {}'.format(i))
