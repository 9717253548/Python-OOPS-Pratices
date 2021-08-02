from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def side(self):
        print("its have many Sides")

class Triangle(Polygon):
    def side(self):
        print("its have three Sides")

class Pentagon(Polygon):
    def side(self):
        print("its have 5 sides")

class Hexagon(Polygon):
    def side(self):
        print("its have 6 side")


c = Pentagon()
c.side()