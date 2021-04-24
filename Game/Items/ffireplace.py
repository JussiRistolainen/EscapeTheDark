from Game.Items.fitem import Item


class Fireplace(Item):

    def __init__(self, window, x, y, name, box, sprite, size, time, delete, liftable):
        super(Fireplace, self).__init__(window, x, y, name, box, delete, liftable)
        self.size = size
        self.time = time
        self.sprite = sprite

    def get_radius(self):
        if self.size*40-self.time > 0:
            return self.size*40-self.time
        else:
            return 0

    def draw_sprite(self):
        if self.size >= 6:
            self.window.blit(self.sprite[0][5], (
                self.get_position_x() - 3 - self.sprite[1] // 2,
                self.get_position_y() - 25 - self.sprite[1] // 2))
        elif self.size >= 3:
            self.window.blit(self.sprite[0][4], (
                self.get_position_x()-3 - self.sprite[1] // 2,
                self.get_position_y()-25 - self.sprite[1] // 2))
            #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.get_position_x()-30, self.get_position_y()-80, 60, 80))



        elif self.size == 2:
            self.window.blit(self.sprite[0][3], (
                self.get_position_x() - 3 - self.sprite[1] // 2,
                self.get_position_y() - 25 - self.sprite[1] // 2))
        elif self.size == 1:
            self.window.blit(self.sprite[0][2], (
                self.get_position_x() - 3 - self.sprite[1] // 2,
                self.get_position_y() - 25 - self.sprite[1] // 2))
        elif self.size == 0:
            self.window.blit(self.sprite[0][0], (
                self.get_position_x() - 3 - self.sprite[1] // 2,
                self.get_position_y() - 25 - self.sprite[1] // 2))


    def add_log(self):
        self.size += 1

    def update_time(self):
        self.time += 0.1
        if self.time >= 60 and self.size >= 1:
            self.time = 0
            self.size -= 1








