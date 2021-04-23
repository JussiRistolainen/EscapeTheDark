import pygame


class Display:

    def __init__(self, window, icon, IMAGES):
        self.window = window
        self.time = 0
        self.icon = icon
        self.sort_list = []
        self.IMAGES = IMAGES

    def update(self, object_list):
        draw_character = 0
        self.sort_list = sorted(object_list, key=lambda x: x.get_position_y())
        for i in self.sort_list:
            if i.name != "torch":
               i.draw_sprite()

    def update_icon(self, pos):
        if 4 < pos[0] < 35 and 289 < pos[1] < 310:
            self.icon = 1
        elif 4 < pos[0] < 35 and 311 < pos[1] < 330:
            self.icon = 2
        elif 4 < pos[0] < 35 and 331 < pos[1] < 370:
            self.icon = 3
        else:
            self.icon = 0

    def get_icon(self):
        return self.icon

    def update_overlay(self):
        self.draw_sprite(100, 2, 2, 'log_index0', 165, 45)
        self.draw_sprite(80, 2, 2, 'matchbox_count0', 220, 30)
        self.draw_sprite(40, 2, 2, 'log_icon0', 20, 300)
        self.draw_sprite(40, 2, 2, 'matchbox_icon0', 17, 320)
        self.draw_sprite(40, 2, 2, 'torch0', 17, 350)
        if self.icon == 1:
            self.draw_sprite(40, 2, 2, 'log_icon_checked0', 20, 300)
        elif self.icon == 2:
            self.draw_sprite(40, 2, 2, 'matchbox_icon_checked0', 17, 320)
        elif self.icon == 3:
            self.draw_sprite(40, 2, 2, 'torch_checked0', 17, 350)

    def draw_sprite(self, object_size, x_div, y_div, sprite_name, pos_x, pos_y):
        self.window.blit(self.IMAGES[0][sprite_name], (pos_x - object_size // x_div, pos_y - object_size // y_div))




