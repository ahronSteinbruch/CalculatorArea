
class Shape:

    def get_area(self):
        pass
    def get_perimeter(self):
        pass
    def __eq__(self, other):
        return self.get_area() == other.get_area() and self.get_perimeter() == other.get_perimeter()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()
    def __add__(self, other):
        return self.get_area() + other.get_area()
