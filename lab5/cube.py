from solid_shape import SolidShape
from square import Square

class Cube(SolidShape, Square):
    def __init__(self, side):
        Square.__init__(self, side)

    def volume(self):
        return self.length ** 3
