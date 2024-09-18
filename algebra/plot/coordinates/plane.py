
from plot.shape import Shape, Plane


class AxisPlane(Shape):

    def __init__(self, axis, color='orange', opacity=0.2):
        super().__init__(color, opacity)
        if axis == 'x':
            self.plane =  Plane( (1,0,0,0), color=color, opacity=opacity)
        if axis == 'y':
            self.plane =  Plane( (0,1,0, 0), color=color, opacity=opacity)
        if axis == 'z':
            self.plane =  Plane( (0,0,1, 0), color=color, opacity=opacity)

    def draw(self, canvas):
        self.plane.draw(canvas)