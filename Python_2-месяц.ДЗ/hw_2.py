class Figure:
    unit = "cm"

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

    def info(self):
        raise NotImplementedError("Subclasses must implement this method")
class Circle(Figure):

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius


    def calculate_area(self):
        return (self.__radius ** 2) * 3.14

    def info(self):
        print(f"Circle radius: {self.__radius}{self.unit}, "
              f"area: {self.calculate_area()}{self.unit}²")

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return (self.__side_a * self.__side_b) / 2

    def info(self):
        print(f'RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, '
              f'area: {self.calculate_area()}{self.unit}²')


circles = [Circle(2), Circle(5)]
right_triangles = [RightTriangle(5, 8),RightTriangle(3, 4), RightTriangle(10, 12)]

for figure in circles + right_triangles:
    figure.info()
print('-----------------------ДЗ**-----------------------------')
class Square(Figure):

    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
        self.__perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def calculate_perimeter(self):
        return 4 * self.__side_length

    def info(self):
        print(f"Square side length: {self.__side_length}{self.unit}, "
              f"perimeter: {self.__perimeter}{self.unit}, "
              f"area: {self.calculate_area()}{self.unit}")


class Rectangle(Figure):

    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
        self.__perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def info(self):
        print(f"Rectangle length: {self.__length}{self.unit}, "
              f"width: {self.__width}{self.unit}, "
              f"perimeter: {self.__perimeter}{self.unit}, "
              f"area: {self.calculate_area()}{self.unit}²")





squares = [Square(5), Square(10)]
rectangles = [Rectangle(5, 8), Rectangle(10, 15), Rectangle(20, 25)]

for figure in squares + rectangles:
    figure.info()

print('-----------------------ДЗ*-----------------------------')

