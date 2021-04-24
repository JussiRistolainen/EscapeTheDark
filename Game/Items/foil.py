from Game.Items.fitem import Item
import pygame

class Oil(Item):

    def __init__(self, window, x, y, name, box, sprite, delete, liftable):
        super(Oil, self).__init__(window, x, y, name, box, delete, liftable)
        self.sprite = sprite
        self.time = 0

    def draw_sprite(self):
        self.time += 0.1
        self.window.blit(self.sprite[0], (
            self.get_position_x()+30 - self.sprite[1] // 2,
            self.get_position_y()+32 - self.sprite[1] // 2))
        #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.get_position_x()-15, self.get_position_y()-20, 11, 30))


