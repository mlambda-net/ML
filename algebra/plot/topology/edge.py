import numpy as np


class Edge :
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @property
    def vector(self):
        vector = tuple(e - s for s, e in zip(self.start.vector, self.end.vector))
        return  np.array(vector)

