import pygame
import os
import sys

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


# <<< background
background_width, background_height = SIZE
background = pygame.transform.smoothscale(load_image('background.png'), (background_width, background_height))
# <<<


pos_x = 0  # <<< Позиция старта
speed = 3  # <<< Скорость движения

start_flag = False  # <<< Флаг старта движения

pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Начало движение (SPACE) <<<
    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_SPACE]:
        start_flag = True
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
    pygame.display.flip()

pygame.quit()
