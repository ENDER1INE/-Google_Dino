import os
import sys
import random

import pygame.mask

from game_parts import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def random_x_coord(self):
    return random.randint(1000, 2200)


screen_rect = (0, 0, 1000, 400)


class Stone(pygame.sprite.Sprite):
    stone = load_image("stone.png")
    stone = pygame.transform.scale(stone, (20, 35))
    spawn_stone = False
    contact = False
    speed_object = 9

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Stone.stone
        x_coord = random_x_coord(self)
        list_coords_spawn.append(x_coord)
        self.rect = pygame.rect.Rect(x_coord, 315, 20, 30)
        self.rect.x, self.rect.y = x_coord, 315
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(-Stone.speed_object, 0)
        if self.rect.right < 0:
            self.kill()


class Cactus(pygame.sprite.Sprite):
    cactus = load_image('cactus.png')
    cactus = pygame.transform.scale(cactus, (25, 40))
    speed_object = 9

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Cactus.cactus
        x_coord = random.randint(1000, 1500)
        list_coords_spawn.append(x_coord)
        self.rect = pygame.rect.Rect(x_coord, 305, 20, 35)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(-Cactus.speed_object, 0)
        if self.rect.right < 0:
            self.kill()