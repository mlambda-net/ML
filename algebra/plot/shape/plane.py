import numpy as np
import pyvista as pv

from plot.shape import Shape


class Plane(Shape):

    def __init__(self,plane, color='orange', opacity=0.2):
        super().__init__(color, opacity)
        self.plane = plane


    def draw(self, canvas):
        (A, B, C, D ) = self.plane
        normal = (A, B, C)

        if C != 0:
            point = (0, 0, -D / C)
        else:
            # Handle the case where C is 0 (e.g., A = 1, B = 1, C = 0, D = -10) which could be a plane parallel to Z-axis
            if A != 0:
                point = (-D / A, 0, 0)
            elif B != 0:
                point = (0, -D / B, 0)
            else:
                raise ValueError("Invalid plane equation coefficients")


        plane = pv.Plane(center= np.array(point), direction=np.array(normal), i_size=5, j_size=5)
        canvas.render(plane, color=self.color, opacity=self.opacity)
