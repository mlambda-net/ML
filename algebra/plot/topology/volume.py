class Volume:
    def __init__(self, surfaces):
        self.surfaces = surfaces  # list of Faces or Planes

    def __repr__(self):
        return f"Volume(surfaces={self.surfaces})"

