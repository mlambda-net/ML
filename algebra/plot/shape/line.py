import numpy as np
import pyvista as pv

from plot.shape import Shape


class Line(Shape):
    def __init__(self, origin=[0,0,0], destination=[0,0,0], color='blue', opacity=0.7):

        super().__init__(color, opacity)
        self.origin = np.array(origin)
        self.destination = np.array(destination)

    def draw(self, canvas):
        # Create the line
        line = pv.Line(self.origin, self.destination)
        canvas.render(line, color='blue', line_width=2)

