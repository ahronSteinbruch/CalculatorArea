from Shape import Shape


class Rectangle (Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return f"Rectangle: height = {self.height}, width = {self.width}, area = {self.get_area()}, perimeter = {self.get_perimeter()}"

