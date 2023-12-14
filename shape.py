from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_perimeter(self) -> float:
        pass

    @abstractmethod
    def calc_area(self) -> float:
        pass
