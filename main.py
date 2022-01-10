import pygame
import os
import sys
import random

from dinozavr import Dino
from objects import Objects

SIZE = WIDTH, HEIGHT = 1000, 400


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def time_speed_up():  # <<< функция счета секунд
    return int(pygame.time.get_ticks()) // 1000


dino_sprite = pygame.sprite.Group()
drag = Dino(load_image("dino_anim.png"), 5, 2, 20, 270, dino_sprite)
#drag_jump = Dino(load_image("1_2_string.png"), 5, 2, 20, 270, dino_sprite)

objects_sprites = pygame.sprite.Group()
Objects(objects_sprites)

# <<< background
background_width, background_height = SIZE
background = pygame.transform.smoothscale(load_image('background.png'), (background_width, background_height))
# <<<


pos_x = 0  # <<< Позиция старта
speed = 3  # <<< Скорость движения
isJump = False
jumpCount = 10
start_flag = False  # <<< Флаг старта движения

pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
clock = pygame.time.Clock()
fps = 60
count = 0
while running:
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
    if start_flag:
        pos_x -= speed
    # >>>

    #  Увеличение скорости каждые 2 сек
    if time_speed_up() % 2 == 0:
        speed += 0.001
    # >>>

    #  Движение заднего фона <<<
    coord_image_1 = pos_x % background_width
    coord_image_2 = coord_image_1 - background_width if coord_image_1 > 0 else coord_image_1 + background_width
    screen.blit(background, (coord_image_1, 0)), screen.blit(background, (coord_image_2, 0))
    # >>>
    dino_sprite.draw(screen)
    objects_sprites.draw(screen)
    if start_flag:
        objects_sprites.update()
        drag.jump()
        dino_sprite.update()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
