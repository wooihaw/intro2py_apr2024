# -*- coding: utf-8 -*-
"""


@author: wooihaw
"""

class Circle:
    __pi = 3.14159
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return Circle.__pi * self.radius ** 2
    def circumference(self):
        return 2 * Circle.__pi * self.radius
    
c = Circle(4)
print(c.area(), c.circumference(), sep=", ")
