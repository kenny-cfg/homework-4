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


class Square(Shape):
    def __init__(self, a: int):
        self.length = a

    def calc_perimeter(self) -> float:
        return 4 * self.length

    def calc_area(self) -> float:
        return self.length * self.length
