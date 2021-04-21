import pygame
from ftime import Timecount
from Game.fbackground import Background
from fcharacter import Character
from fdisplay import Display
from fitem_controller import Item_control
from ffireplace import Fireplace
import Interaction_controller


def main():
    pygame.init()

    res_w = 1280
    res_h = 720
    window = pygame.display.set_mode((res_w, res_h))
    running = True
    FPS = 30
    icon = 0

    #Item list
    object_list = []
    fire_list = []

    images = load_images()
    #Single_objects
    time_count = Timecount(window, res_w, res_h, 0, 0, 0, 1)
    item_methods = Item_control(window, object_list, fire_list, icon, res_w, res_h, images)
    background = Background(window)
    display = Display(window, 0, images)

    #GameClock
    Clock = pygame.time.Clock()
    CLOCKTICKFLAME = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOCKTICKFLAME, 100)

    game_start(window, object_list, images, item_methods)
    mouse = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()

            x_force = 0
            y_force = 0
            if keys[pygame.K_LEFT]:
                x_force = -20

            if keys[pygame.K_RIGHT]:
                x_force = 20

            if keys[pygame.K_UP]:
                y_force = -20

            if keys[pygame.K_DOWN]:
                y_force = 20

            update_character_speed(object_list[0], x_force, y_force)

            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0] == 1 and mouse:
                Interaction_controller.clicked(display.get_icon(), time_count, item_methods, pos)
                mouse = 0
                display.update_icon(pos)
            if event.type == CLOCKTICKFLAME:
                update_game_overlay(time_count, background, display, fire_list, item_methods)
                delete_items(object_list, fire_list)
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = 1

        Clock.tick(FPS)


def update_game_overlay(time_count, background, display, fire_list, item_methods):
    time_count.update_time()
    item_methods.update_flames_time()
    background.update(fire_list)
    time_count.update_overlay()
    display.update(item_methods.seen_items())
    display.update_overlay()
    pygame.display.flip()


def update_character_speed(character, x, y):
    character.update_character_pos(character.speed(x, y))


def game_start(window, object_list, images, item_methods):
    lumberjack_key = [images[0].get(key) for key in ['Lumberjack0', 'Lumberjack1']]
    object_list.append(Character(window, 300, 300, 0, 0, [0, 0, 0, 0], "character", [lumberjack_key, images[1][0]], False))

    item_methods.create_log(1)
    item_methods.create_fire_place([500, 500])


def delete_items(object_list, fire_list):
    delete_list = []
    for index, i in enumerate(object_list):
        if i.delete:
            delete_list.append(index)
    for i in delete_list:
        object_list.pop(i)
    delete_list = []
    for index, i in enumerate(fire_list):
        if i.delete:
            delete_list.append(index)
    for i in delete_list:
        fire_list.pop(i)


def load_images():
    image_list = ['Lumberjack', 'spritelog', 'logburn', 'log_index', 'matchbox',
                  'log_icon', 'log_icon_checked', 'matchbox_icon', 'matchbox_icon_checked', 'sprite_',
                  'sprite22_', 'sprite2_', 'fireplace']
    index_list = [2, 1, 3, 1, 1,
                  1, 1, 1, 1, 13,
                  4, 4, 6]
    image_size = [200, 100, 120, 60, 60,
                  40, 40, 40, 40, 120,
                  120, 120, 120]
    IMAGES = {}
    for index, p in enumerate(image_list):
        for i in range(0, index_list[index]):
            IMAGES[p + str(i)] = pygame.transform.scale(
                pygame.image.load('Game/Images/log/' + p + str(i) + '.png'), (image_size[index], image_size[index]))
    return IMAGES, image_size


if __name__ == "__main__":
    main()
