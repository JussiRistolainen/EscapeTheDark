import math


class Position(object):
    def __init__(self, x, y, box):
        self.x = x
        self.y = y
        self.box = box

    def get_position(self):
        return self

    def get_position_x(self):
        return self.x

    def get_position_y(self):
        return self.y

    def get_distance_from_position(self, point):
        return math.sqrt(
            (self.x - point[0]) * (self.x - point[0])
            + (self.y - point[1]) * (self.y - point[1])
        )

    def get_box(self):
        return self.box

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y