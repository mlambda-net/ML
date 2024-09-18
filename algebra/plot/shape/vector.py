import numpy as np
import pyvista as pv

from plot.shape import Shape


class Vector(Shape):
    def __init__(self, origin=[0,0,0], destination = [0,1,0], mag=1, color='green', opacity=1):
        super().__init__(color, opacity)
        self.origin = origin
        self.destination = destination
        self.mag = mag

    def draw(self, canvas):

        arrow = pv.Arrow(
            np.array(self.origin),
            np.array(self.destination),
            tip_radius=0.01,
            tip_length=0.01,
            shaft_radius=0.0009
        )

        canvas.render(arrow, color=self.color, opacity=self.opacity)