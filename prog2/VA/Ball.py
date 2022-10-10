import numpy as np
class Ball:

    def __init__(self, size, spd_x, spd_y, pos_x, pos_y, color):
        self.size = size
        self.speed = np.array(spd_x, spd_y)
        self.pos = np.array(pos_x, pos_y)
        self.color = color


