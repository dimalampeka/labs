from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from cube import Cube
from sphere import Sphere

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, params):
        shape_classes = {
            "circle": Circle,
            "rectangle": Rectangle,
            "square": Square,
            "triangle": Triangle,
            "cube": Cube,
            "sphere": Sphere
        }
        if shape_type in shape_classes:
            return shape_classes[shape_type](*params)
        return None
