from Game.Items.fitem import Item


class Character(Item):

        def __init__(self, window, x, y, x_speed, y_speed, box, name, sprite, delete, item, liftable):
            super(Character, self).__init__(window, x, y, name, box, delete, liftable)
            self.x_speed = x_speed
            self.y_speed = y_speed
            self.sprite = sprite
            self.time = 0
            self.item = item

        def update_character_pos(self, change):
            self.x += change[0]
            self.y += change[1]
            if self.item is not None:
                if self.item.name == "torch":
                    self.item.set_x(self.x)
                    self.item.set_y(self.y)

        def speed(self, x_force, y_force):
            if x_force > 0:
              self.x_speed = 5
            if x_force == 0:
                self.x_speed = 0
            if x_force < 0:
                self.x_speed = -5
            if y_force > 0:
                self.y_speed = 5
            if y_force == 0:
                self.y_speed = 0
            if y_force < 0:
                self.y_speed = -5

            return self.x_speed, self.y_speed

        def draw_sprite(self):
            self.time += 0.1
            if self.item is None:
                self.window.blit(self.sprite[0][0][int(self.time % 2)], (
                    self.get_position_x() - self.sprite[1] // 2,
                    self.get_position_y()-10 - self.sprite[1] // 1.6))
            elif self.item.name == "torch":
                self.window.blit(self.sprite[0][1][int(self.time % 3)], (
                    self.get_position_x()+15 - self.sprite[1] // 2,
                    self.get_position_y() - 5 - self.sprite[1] // 1.6))
                #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.get_position_x(), self.get_position_y(), 1, 1))




        def set_item(self, item):
            self.item = item

        def check_item(self):
            if self.item != None:
                 if self.item.size == 0:
                    self.item = None

