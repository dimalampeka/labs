import math
from solid_shape import SolidShape
from circle import Circle

class Sphere(SolidShape, Circle):
    def __init__(self, radius):
        Circle.__init__(self, radius)

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)
