import pygame
import os
import sys


SIZE = WIDTH, HEIGHT = 1800, 700


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


all_sprites = pygame.sprite.Group()
Dino(all_sprites)

background_width, background_height = SIZE
background = pygame.transform.smoothscale(pygame.image.load('background.png'), (background_width, background_height))

pos_x = 0  # <<< Позиция старта
speed = 15  # <<< Скорость движения

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

    #  Движение заднего фона <<<
    coord_image_1 = pos_x % background_width
    coord_image_2 = coord_image_1 - background_width if coord_image_1 > 0 else coord_image_1 + background_width
    screen.blit(background, (coord_image_1, 0))
    screen.blit(background, (coord_image_2, 0))
    pygame.display.flip()
    all_sprites.draw(screen)
    # >>>
pygame.quit()
