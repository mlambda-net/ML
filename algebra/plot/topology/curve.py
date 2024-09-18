# Curve class
class Curve:
    def __init__(self, points):
        self.points = points  # list of control points or a function

    def __repr__(self):
        return f"Curve(points={self.points})"
