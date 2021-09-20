import numpy as np

class rope:
    """A class containing necessary information and behaviors for the rope (lines) of the simulation."""

    def __init__(self, color = (255, 255, 255), width=2, length = 100, theta = np.pi/4, start = [0, 0]):
        self.color = color
        self.width = width
        self._length = length
        self.theta = theta
        self.start = start
        self.end = [start[0], self.length]

    @property
    def length(self):
        return self._length

    @property
    def theta(self):
        return self._theta

    @property
    def start(self):
        return self._start # an underscore denotes private variables

    @property
    def end(self):
        return self._end

    @theta.setter
    def theta(self, new_theta):
        self._theta = new_theta

    @start.setter
    def start(self, new_start):
        if len(new_start) != 2:
            raise ValueError('Starting point must be a list of 2 X, Y coordinates')
        self._start = np.abs(new_start)
    
    @end.setter
    def end(self, new_end):
        if len(new_end) != 2:
            raise ValueError('Ending point must be a list of 2 X, Y coordinates')
        self._end = np.abs(new_end)
    
    def swing(self):
        x = np.cos(self.theta) * self.length + self.start[0]
        y = np.sin(self.theta) * self.length + self.start[1]
        self.end = [x, y]
