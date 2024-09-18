import numpy as np
import pyvista as pv

from plot.shape import Shape


class Polygon(Shape):
    def __init__(self, points, color='red', opacity=1):

        super().__init__(color, opacity)
        self.points = np.array(points)

    def draw(self, canvas):
        polygon = np.array([range(len(self.points))], dtype=np.intp)
        faces = np.hstack([[len(self.points)], polygon[0]])
        polygon = pv.PolyData(self.points, faces)
        canvas.render(polygon, color=self.color, opacity=self.opacity, style='wireframe')
        for point in self.points:
            canvas.add_label(point,  f"({point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f})" )

