import numpy as np
from flog import Burn
from fflame import Flame
from ffireplace import Fireplace

class Item_control:

    def __init__(self, window, object_list, fire_list, icon, res_w, res_h, images):
        self.window = window
        self.object_list = object_list
        self.fire_list = fire_list
        self.icon = icon
        self.res_w = res_w
        self.res_h = res_h
        self.images = images

        self.fire_key1 = [self.images[0].get(key) for key in ['logburn0', 'logburn1', 'logburn2']]
        self.fire_key2 = [self.images[0].get(key) for key in ['sprite22_0', 'sprite22_1', 'sprite22_2', 'sprite22_3']]
        self.fire_key4 = [self.images[0].get(key) for key in ['sprite_0', 'sprite_1', 'sprite_2', 'sprite_3', 'sprite_4', 'sprite_5', 'sprite_6',
                                                              'sprite_7', 'sprite_8', 'sprite_9', 'sprite_9', 'sprite_10', 'sprite_11', 'sprite_12']]
        self.fire_key3 = [self.images[0].get(key) for key in ['sprite2_0', 'sprite2_1', 'sprite2_2', 'sprite2_3']]
        self.log_key = self.images[0].get('spritelog0')
        self.fire_place = [self.images[0].get(key) for key in ['fireplace0', 'fireplace1', 'fireplace2', 'fireplace3', 'fireplace4', 'fireplace5']]

    def create_fire_place(self, pos):
        obj = Fireplace(self.window, pos[0], pos[1], "FirePlace", [pos[0]-30, pos[1]-60, pos[0]+30, pos[1]+20], [self.fire_place, self.images[1][12]], 3, 0, False)
        self.object_list.append(obj)
        self.fire_list.append(obj)


    def create_log(self, number):
        for i in range(number):
            random_x = np.random.randint(self.res_w - 200) + 100
            random_y = np.random.randint(self.res_h - 200) + 100
            self.object_list.append(Burn(self.window, random_x, random_y, "Log", [random_x - 40, random_y - 18, random_x + 45, random_y + 12], [self.log_key, self.images[1][2]], False))

    def create_fire(self, pos):
        obj = Flame(self.window, pos[0], pos[1], "bondfire", [pos[0] - 38, pos[1] - 25, pos[0] + 27, pos[1]], [[self.fire_key1, self.fire_key2, self.fire_key3, self.fire_key4], self.images[1][2]], 3, 0, False)
        self.object_list.append(obj)
        self.fire_list.append(obj)



    def create_log_with_pos(self, pos):
        picked = True
        for i in self.object_list:
            if i.box[0] < pos[0] < i.box[2] and i.box[1] < pos[1] < i.box[3] and (i.name == 'bondfire' or i.name == "FirePlace"):
                i.add_log()
                picked = False
        if picked:
            self.object_list.append(Burn(self.window, pos[0], pos[1], "Log", [pos[0] - 40, pos[1] - 18, pos[0] + 45, pos[1] + 12], [self.images[0]['spritelog0'], self.images[1][2]], False))

    def check_for_log(self, pos):
        picked = True
        for index, i in enumerate(self.object_list):
            if picked:
                if (i.box[0] < pos[0] < i.box[2]) and (i.box[1] < pos[1] < i.box[3]):
                    if i.name == "Log":
                        self.object_list.pop(index)
                        obj = Flame(self.window, pos[0], pos[1], "bondfire", [pos[0] - 38, pos[1] - 22, pos[0] + 27, pos[1]], [[self.fire_key1, self.fire_key2, self.fire_key3, self.fire_key4], 120], 1, 0, False)
                        self.object_list.append(obj)
                        self.fire_list.append(obj)
                        picked = False

    def seen_items(self):
        seen_items = []
        for i in self.fire_list:
            for p in self.object_list:
                if p.get_distance_from_position((i.get_position_x(), i.get_position_y())) < i.get_radius():
                    seen_items.append(p)
        return seen_items

    def lift_item(self, time_count, pos):
        del_item = -1
        lifted = True
        for index, i in enumerate(self.object_list):
            if lifted:
                if i.is_clicked(pos) and (i.name != "bondfire" or i.name != "FirePlace"):
                    del_item = index
                    time_count.add_item(i.name)
                    lifted = False
        if del_item != -1:
            self.object_list.pop(del_item)

    def update_flames_time(self):
        for i in self.fire_list:
            i.update_time()
