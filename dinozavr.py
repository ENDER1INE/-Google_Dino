import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Dino(pygame.sprite.Sprite):
    dinosaur = load_image("images.jpeg")

    def __init__(self, *group):
        super().__init__(*group)
        self.dinosaur = Dino.dinosaur
        self.rect = self.dinosaur.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def update(self):
       pass
