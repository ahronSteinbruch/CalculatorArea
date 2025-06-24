from Shape import Shape

class Square (Shape):
    def __init__(self,side):
        self.side = side

    def get_area(self):
        return self.side**2

    def get_perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"Square: height = {self.side}, width = {self.side}, area = {self.get_area()}, perimeter = {self.get_perimeter()}"



