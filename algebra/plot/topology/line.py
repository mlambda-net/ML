
class Line:
    def __init__(self, point, direction):
        self.point = point
        self.direction = direction  # as a vector

    def __repr__(self):
        return f"Line(point={self.point}, direction={self.direction})"

