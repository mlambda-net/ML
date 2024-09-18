class Shape:

    def __init__(self, color, opacity):
        self.color = color
        self.opacity = opacity


    def draw(self, canvas):
        raise NotImplementedError("This method should be overridden by subclasses")

