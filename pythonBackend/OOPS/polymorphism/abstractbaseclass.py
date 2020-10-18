# An abstract base class is a class which doesn't have definition on it's own, it has the abstract methods
# which forces the implementation in it's derived class
from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4

    def area(self):
        print("area of square", self.side * self.side)


class Rectangle(Shape):
    length = 4
    breadth = 10

    def area(self):
        print("area of Rectanle", self.length * self.breadth)


sq = Square()
sq.area()
rec = Rectangle()
rec.area()
