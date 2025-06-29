from Shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def __str__(self):
        return f"Circle: radius = {self.radius}, area = {self.get_area()}, perimeter = {self.get_perimeter()}"