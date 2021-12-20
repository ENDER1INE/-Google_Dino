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


background_width, background_height = SIZE
bg = pygame.transform.smoothscale(pygame.image.load('back.png'), (background_width, background_height))
pos_x = 0
speed = 10

pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    allKeys = pygame.key.get_pressed()
    pos_x += speed if allKeys[pygame.K_LEFT] else -speed if allKeys[pygame.K_RIGHT] else 0

    x_rel = pos_x % background_width
    x_part2 = x_rel - background_width if x_rel > 0 else x_rel + background_width

    screen.blit(bg, (x_rel, 0))
    screen.blit(bg, (x_part2, 0))
    pygame.display.flip()
pygame.quit()