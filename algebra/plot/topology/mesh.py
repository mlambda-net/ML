# Mesh class
class Mesh:
    def __init__(self, vertices, edges, faces):
        self.vertices = vertices  # list of Points
        self.edges = edges  # list of Edges
        self.faces = faces  # list of Polygons

    def __repr__(self):
        return f"Mesh(vertices={self.vertices}, edges={self.edges}, faces={self.faces})"

