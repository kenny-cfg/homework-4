import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_perimeter(self) -> float:
        pass

    @abstractmethod
    def calc_area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, a: int, b: int):
        self.length = a
        self.width = b

    def calc_perimeter(self) -> float:
        return 2 * (self.length + self.width)

    def calc_area(self) -> float:
        return self.length * self.width


# I know the UML diagram inherits from Shape directly, but this is nicer.
class Square(Rectangle):
    def __init__(self, a: int):
        super().__init__(a, a)


class RightAngledTriangle(Shape):
    def __init__(self, height: int, base: int):
        self.height = height
        self.base = base

    def calc_perimeter(self) -> float:
        hypotenuse_squared = self.height ** 2 + self.base ** 2
        hypotenuse = math.sqrt(hypotenuse_squared)
        return self.base + self.height + hypotenuse

    def calc_area(self) -> float:
        return (self.base * self.height) / 2
