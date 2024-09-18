import pyvista as pv
import numpy as np


class Render:

    def __init__(self, plotter):
        self.translate =  np.array([
            [1, 0, 0, 0],  # Keep X as is
            [0, 0, -1, 0],  # Swap Y and Z (Y becomes Z)
            [0, 1, 0, 0],  # Swap Y and Z (Z becomes -Y for mirroring effect)
            [0, 0, 0, 1]  # Homogeneous coordinate
        ])
        self.plotter = plotter

    def render(self, mesh, *args, **kwargs):
        #self.plotter.add_mesh(mesh, *args, **kwargs)
        self.plotter.add_mesh(mesh.transform(self.translate), *args, **kwargs)

    def add_label(self, position, label):
        point = np.append(position, 1)
        new_point = self.translate @ point
        label = pv.Label(text= label, position=new_point[:3], size=12)
        self.plotter.add_actor(label)

class Viewer:
    def __init__(self, size=None,title="Visual", notebook=False ):

        if size is None:
            
            size = [1024, 768]
        self.plotter = pv.Plotter(image_scale=1, window_size=size, title=title, notebook=notebook)
        self.plotter.camera_position = [
            (5, 0, 0),  # Camera location: Along the X-axis
            (0, 0, 0),  # Focal point: Origin
            (0, -1, 1)  # Inverted Y and Z axes: Z is up and Y is to left
        ]
        self.render = Render(self.plotter)
       # self.plotter.background_color = 'black'
        self.plotter.show_axes()
        self.plotter.view_isometric()


    def draw(self, shape):
        shape.draw(self.render)

    def setup_event_handlers(self):
        # Handle mouse click events
        self.plotter.track_click_position(callback=self.on_mouse_click, side="left")
        # Handle key press events
        keys = ['a', 's', 'd', 'w',]
        for key in keys:
            self.plotter.add_key_event(key, self.on_key_press(key))

        self.plotter.add_key_event('r', lambda : self.plotter.view_isometric())

    def on_mouse_click(self, event):
        print(f"Mouse clicked at position: {event.position}")

    def on_key_press(self, key):
        return lambda: print(f"{key.upper()} key pressed")

    def run(self):
        self.setup_event_handlers()
        self.plotter.show()

