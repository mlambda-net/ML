class Plane:
    def __init__(self, point, normal):
        self.point = point
        self.normal = normal  # as a vector

    def __repr__(self):
        return f"Plane(point={self.point}, normal={self.normal})"
