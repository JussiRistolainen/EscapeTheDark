from Game.Items.fposition import Position


class Item(Position):
    def __init__(self, window, x, y, name, box, delete, liftable):
        super(Item, self).__init__(x, y, box)
        self.window = window
        self.name = name
        self.delete = False
        self.liftable = liftable


    def get_name(self):
        return self.name

    def is_clicked(self, pos):
        return (self.box[0] < pos[0] < self.box[2]) and (self.box[1] < pos[1] < self.box[3])

    def is_liftable(self):
        return self.liftable



