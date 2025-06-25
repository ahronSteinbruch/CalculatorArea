from Rectangle import Rectangle
class Right_angled_triangle(Rectangle):
    def __init__(self, height, width):
        super().__init__(height, width)

    def get_area(self):
        return super().get_area()/2

    def get_perimeter(self):
        return super().width + super().height + ((super().height**2 + super().width**2)**0.5)

    def __str__(self):
        return f"Right_angled_triangle: height = {self.height}, width = {self.width}, area = {self.get_area()}, perimeter = {self.get_perimeter()}"