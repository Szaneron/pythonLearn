"""
    Stwórz trzy klasy:
    1) Rectangle - prostokąt
    2) Square - kwadrat
    3) Cube - sześcian

    a) Stwórz konstruktory (__init__)
    b) metody obliczające powierzchnię kwadratu, prostokąta, sześcianu
    c) metodę obliczającą objętość sześcianu

    Zastanów się jak możesz wykorzystać do tego dziedziczenie, aby nie powtarzać kodu
"""
""" 
    association - mapping meaning: belongs to, is one of the components, is part of something
    
    Aggregation - combine, concatenate, accumulate - create a component object
    
    Composition - same as aggregation with ONE CONDITION - the object that we assign cannot exist without the class to which this object is assigned to
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, sideLength):
        super(Square, self).__init__(sideLength, sideLength)


class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def count_volume(self):
        return self.base.count_surface_area() * self.height

    def count_surface_area(self):
        return 2 * self.base.count_surface_area() + 2 * self.base.width * self.height + 2 * self.base.height * self.height


class Cube():
    def __init__(self, square: Square):
        self.square = square

    def count_surface_area(self):
        return self.square.count_surface_area() * 6

    def count_volume(self):
        return self.square.count_surface_area() * self.square.height


print(Rectangle(5, 3).count_surface_area())
print(Square(4).count_surface_area())
print(Cube(Square(2)).count_surface_area())
print(Cuboid(Rectangle(5, 3), 5).count_volume())
