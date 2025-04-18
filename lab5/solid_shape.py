from shape import Shape
from abc import ABC, abstractmethod

class SolidShape(Shape, ABC):
    @abstractmethod
    def volume(self):
        pass
