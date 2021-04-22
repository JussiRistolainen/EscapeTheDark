import pygame
from fitem import Item


class Torch(Item):

    def __init__(self, window, x, y, name, box, sprite, size, time, delete, liftable):
        super(Torch, self).__init__(window, x, y, name, box, delete, liftable)
        self.size = size
        self.time = time
        self.sprite = sprite

    def get_radius(self):
        return self.size*90-self.time


    def update_time(self):
        self.time += 0.1
        if self.time >= 60 and self.size == 1:
            self.delete = True
            self.size = 0
            self.time = 0








