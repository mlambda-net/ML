import numpy as np
import pyvista as pv

from plot.shape import Shape


class Point(Shape ):
    def __init__(self,position=[0,0,0], size= 2 ,color='black', opacity=1):
        super().__init__(color, opacity)
        self.position = position
        self.size = size

    def draw(self, canvas):
        data = pv.PolyData(np.array(self.position))
        canvas.render(data,
                        color=self.color,
                        opacity=self.opacity,
                        point_size=self.size,
                        render_points_as_spheres=True)

