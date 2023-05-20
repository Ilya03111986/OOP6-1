from abc import ABC, abstractmethod
class TwoDimensionalShape(ABC):
    @abstractmethod
    def area(self):
        pass
class ThreeDimensionalShape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def volume(self):
        pass
class Circle(TwoDimensionalShape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 2 * 3.14 * self.radius
class Cube(ThreeDimensionalShape):
    def __init__(self, edge):
        self.edge = edge
    def area(self):
        return 6 * self.edge * self.edge
    def volume(self):
        return self.edge * self.edge * self.edge
    