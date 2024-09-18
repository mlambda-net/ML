import pyvista as pv

from plot.shape import Shape



class Cylinder(Shape):
    def __init__(self, center=(0, 2, 2), direction=(1, 1, 1), radius=0.5, height=2.0, color='green', opacity=0.5):
        super().__init__(color, opacity)
        self.center = center
        self.direction = direction
        self.radius = radius
        self.height = height


    def draw(self, canvas):
        cylinder = pv.Cylinder(center=self.center, direction=self.direction, radius=self.radius, height=self.height)
        canvas.render(cylinder, color=self.color, opacity=self.opacity)

