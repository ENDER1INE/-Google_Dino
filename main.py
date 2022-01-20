import os
import random
import sys

import pygame.transform

from objects import Stone, Cactus
from dinozavr import Dino
from game_parts import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def time_speed_up():  # <<< функция счета секунд
    return pygame.time.get_ticks() // 1000


objects = pygame.sprite.Group()
stone = Stone(objects)
cactus = Cactus(objects)


dino_sprite = pygame.sprite.Group()
drag = Dino(load_image("dino_anim.png"), 5, 2, 20, 270, dino_sprite)
#  drag_jump = Dino(load_image("1_2_string.png"), 5, 2, 20, 270, dino_sprite)


# <<< background
background_width, background_height = SIZE
background = pygame.transform.smoothscale(load_image('background.png'), (background_width, background_height))
# <<<

pygame.init()
pygame.font.init()

font_1 = pygame.font.Font(None, 36)

while running:
    if start_flag:
        if count_score % 50 == 0:
            speed += 1
            Stone.speed_object += 1
            Cactus.speed_object += 1
            count_score += 10
    text1 = font_1.render(str(count_score), True,
                      (255, 255, 255))
    clock_fps.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Начало движение (SPACE) <<<

    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_SPACE]:
        if count >= 1:
            drag.isJump = True
        start_flag = True
        count += 1

    if time_speed_up() not in list_second:
        list_second.append(time_speed_up())

    if start_flag:
        if not game_over:
            pos_x -= speed

    if len(list_second) % 5 == 0:
        count_score += 10
        list_second.append('space')
        Cactus(objects) if random.randint(1, 2) == 1 else Stone(objects)


    #  Движение заднего фона <<<
    coord_image_1 = pos_x % background_width
    coord_image_2 = coord_image_1 - background_width if coord_image_1 > 0 else coord_image_1 + background_width
    screen.blit(background, (coord_image_1, 0)), screen.blit(background, (coord_image_2, 0))
    # >>>
    dino_sprite.draw(screen)
    objects.draw(screen)

    if Stone.contact:
        start_flag = False
        boom = True
        again = True
        game_over = True

    if game_over:
        if allKeys[pygame.K_SPACE]:
            pygame.time.delay(500)
            objects.remove(objects)
            pos_x = 0
            game_over = False
            Stone.contact = False
            start_flag = True
            boom = False
            count_score = 10
            list_second.clear()
            speed = 9
            Stone.speed_object = 9
            Cactus.speed_object = 9
    print(speed, Cactus.speed_object, Stone.speed_object)

    if start_flag:
        dino_sprite.update()
        objects.update()
        drag.jump()

    if pygame.sprite.spritecollideany(drag, objects):
        Stone.contact = True

    if boom:
        end_game_page = load_image('go.png')
        end_game_page = pygame.transform.scale(end_game_page, (300, 150))
        screen.blit(end_game_page, (340, 100))

    screen.blit(text1, (950, 10))

    pygame.display.update()
    pygame.display.flip()
pygame.quit()
