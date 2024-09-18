import numpy as np


class Point:
    def __init(self, *coordinates):
        x,y, z = coordinates
        self.x = x
        self.y = y
        self.z = z


    def __str__(self):
            return f"({self.x},{self.y},{self.z})"

    def __repr__(self):
        return f"Point{self.x,self.y,self.z}"

    @property
    def vector(self):
        return np.array([self.x, self.y, self.z])