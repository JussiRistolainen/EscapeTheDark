import math
import pygame
from fitem import Item


class Flame(Item):

    def __init__(self, window, x, y, name, box, sprite, size, time):
        super(Flame, self).__init__(window, x, y, name, box)
        self.size = size
        self.time = time
        self.sprite = sprite

    def get_radius(self):
        return self.size*150-self.time

    def draw_sprite(self):
        self.time += 0.1
        self.window.blit(self.sprite[0][int(self.time % 3)], (
            self.get_position_x()-3 - self.sprite[1] // 2,
            self.get_position_y()-8 - self.sprite[1] // 2))
        #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.get_position_x()-38, self.get_position_y()-25, 55, 25))
        #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.get_position_x(), self.get_position_y(), 1, 1))

    def add_log(self):
        self.size += 1








