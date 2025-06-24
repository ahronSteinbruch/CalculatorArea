from Shape import Shape
import math

class Hexagon(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (3 * math.sqrt(3) / 2) * (self.side ** 2)

    def get_perimeter(self):
        return 6 * self.side

    def __str__(self):
        return f"Hexagon: side = {self.side}, area = {self.get_area()}, perimeter = {self.get_perimeter()}"