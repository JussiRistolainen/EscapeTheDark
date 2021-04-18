import pygame
from fitem import Item


class Burn(Item):

    def __init__(self, window, x, y, name, box, sprite):
        super(Burn, self).__init__(window, x, y, name, box)
        self.sprite = sprite
        self.time = 0

    def draw_sprite(self):
        self.time += 0.1
        self.window.blit(self.sprite[0], (
            self.get_position_x() - self.sprite[1] // 2,
            self.get_position_y() - self.sprite[1] // 2))
        #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.get_position_x(), self.get_position_y(), 1, 1))








