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


screen_rect = (0, 0, 1000, 400)


class Stone(pygame.sprite.Sprite):
    stone = load_image("stone.png")
    stone = pygame.transform.scale(stone, (30, 30))
    spawn_stone = False
    contact = False
    speed_object = 7

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Stone.stone
        self.rect = self.stone.get_rect()
        self.rect.x, self.rect.y = random.randint(1000, 2200), 315
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(-Stone.speed_object, 0)
        if self.rect.right < 0:
            self.kill()