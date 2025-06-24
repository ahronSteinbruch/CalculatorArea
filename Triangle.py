from Shape import Shape


class Triangle(Shape):
    def __init__(self, side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        s = (self.side1 + self.side2 + self.side3)/2
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"Triangle: side1 = {self.side1}, side2 = {self.side2}, side3 = {self.side3}, area = {self.get_area()}, perimeter = {self.get_perimeter()}"