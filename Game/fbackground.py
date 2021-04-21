import pygame


class Background:

    def __init__(self, window):
        self.window = window
        self.Darkness = (115, 118, 83)
        self.ground = (20, 20, 0)
        self.alpha_value = 200
        self.value = 100

    def draw_circle_alpha(self, surface, value, radius, position):
        target_rect = pygame.Rect(position, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape_surf, (value, 0, 0, 50), (radius, radius), radius)
        surface.blit(shape_surf, target_rect)

    def make_flame_background(self, time, size, position_x, position_y):
        radius = size * 150 - time * 1.2
        position = (position_x, position_y)
        pygame.draw.circle(self.window, self.ground, position, radius)

    def make_flame(self, window, radius, pos_x, pos_y):
        position = [pos_x, pos_y]
        self.draw_circle_alpha(window, self.value, radius, position)
        self.draw_circle_alpha(window, self.value, radius / 1.5, position)
        self.draw_circle_alpha(window, self.value, radius / 3, position)

    def update(self, object_list):
        # Fill background
        self.window.fill(self.ground)
        s = pygame.Surface((1280, 780))  # the size of your rect
        s.set_alpha(self.alpha_value)  # alpha level
        s.fill((0, 0, 0))  # this fills the entire surface
        self.window.blit(s, (0, 0))
        for i in object_list:
            if i.name == "bondfire":
                self.make_flame(self.window, i.get_radius(), i.get_position_x()-8, i.get_position_y()-10)
            if i.name == "FirePlace":
                self.make_flame(self.window, i.get_radius(), i.get_position_x()-2, i.get_position_y()-10)


