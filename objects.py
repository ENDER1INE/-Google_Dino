import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


clock = pygame.time.Clock()
screen_rect = (0, 0, 1000, 400)


class Objects(pygame.sprite.Sprite):
    stone = load_image("stone.png")
    stone = pygame.transform.scale(stone, (50, 50))
    spawn_stone = False

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Objects.stone
        self.rect = self.stone.get_rect()
        x, y = 1000, 295
        self.rect.x, self.rect.y = x, y

    def update(self):
        self.rect.x -= 3
        if not self.rect.colliderect(screen_rect):
            print('end')
            self.kill()
