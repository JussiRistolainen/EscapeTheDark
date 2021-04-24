from Game.Items.fitem import Item
import pygame

class Lantern(Item):

    def __init__(self, window, x, y, name, box, sprite, size, time, delete, liftable):
        super(Lantern, self).__init__(window, x, y, name, box, delete, liftable)
        self.size = size
        self.time = time
        self.sprite = sprite

    def get_radius(self):
        if self.size*50-self.time > 0:
            return self.size * 50 - self.time
        else:
            return self.size*30-self.time

    def draw_sprite(self):
        self.window.blit(self.sprite[0][int(self.time % 3)], (
            self.get_position_x() - self.sprite[1] // 2,
            self.get_position_y()-15 - self.sprite[1] // 2))
        #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.get_position_x()-10, self.get_position_y()-40, 20, 50))

    def add_log(self):
        self.size += 1

    def update_time(self):
        self.time += 0.1
        if self.time >= 60 and self.size > 1:
            self.time = 0
            self.size -= 1
        elif self.time >= 60 and self.size == 1:
            self.size = 0
            self.time = 0








