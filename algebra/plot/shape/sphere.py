
import pyvista as pv
from plot.shape import Shape


class Sphere(Shape):
    def __init__(self, center=(0, 0, 0), radius=1.0, color='green', opacity=0.3):
        super().__init__(color, opacity)
        self.center = center
        self.radius = radius


    def draw(self, canvas):
        sphere = pv.Sphere(radius=self.radius, center=self.center)
        canvas.render(sphere,
                        color=self.color,
                        style='wireframe',
                        line_width=1,
                        smooth_shading=True,
                        opacity=self.opacity)