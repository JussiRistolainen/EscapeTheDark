import math
import pygame
from fitem import Item


class Flame(Item):

    def __init__(self, window, x, y, name, box, sprite, size, time, delete):
        super(Flame, self).__init__(window, x, y, name, box, delete)
        self.size = size
        self.time = time
        self.sprite = sprite

    def get_radius(self):
        return self.size*150-self.time

    def draw_sprite(self):
        self.window.blit(self.sprite[0][int(self.time % 3)], (
            self.get_position_x()-3 - self.sprite[1] // 2,
            self.get_position_y()-8 - self.sprite[1] // 2))

    def add_log(self):
        self.size += 1

    def update_time(self):
        self.time += 0.1
        if self.time >= 60 and self.size > 1:
            self.time = 0
            self.size -= 1
        elif self.time >= 60 and self.size == 1:
            self.delete = True
            self.size = 0
            self.time = 0








