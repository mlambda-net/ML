
import pyvista as pv
from plot.shape import Shape


class Cube(Shape):
    def __init__(self, center=(2, 2, 0), x_length=1.0, y_length=1.0, z_length=1.0, color='red', opacity=0.5):

        super().__init__(color, opacity)
        self.center = center
        self.x_length = x_length
        self.y_length = y_length
        self.z_length = z_length
        self.color = color
        self.opacity = opacity

    def draw(self, canvas):
        cube = pv.Cube(center=self.center, x_length=self.x_length, y_length=self.y_length, z_length=self.z_length)
        canvas.render(cube, color=self.color, opacity=self.opacity)

