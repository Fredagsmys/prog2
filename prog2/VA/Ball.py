import numpy as np


class Ball:

    def __init__(self, radius, spd_x, spd_y, pos_x, pos_y, color):
        self.radius = radius
        self.speed = np.array([spd_x, spd_y])
        self.pos = np.array([pos_x, pos_y])
        self.color = color
        self.object = None

    def get_pos_x(self):
        return self.pos[0]

    def get_pos_y(self):
        return self.pos[1]

    def get_spd_x(self):
        return self.speed[0]

    def get_spd_y(self):
        return self.speed[1]

    def set_pos_x(self, pos):
        self.pos[0] = pos

    def set_pos_y(self, pos):
        self.pos[1] = pos

    def set_spd_x(self, spd):
        self.speed[0] = spd

    def set_spd_y(self, spd):
        self.speed[1] = spd

    def set_obj(self, obj):
        self.object = obj

    def get_obj(self):
        return self.object
