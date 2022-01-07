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


class Dino(pygame.sprite.Sprite):
    dinosaur = load_image("dino.png")
    dinosaur = pygame.transform.scale(dinosaur, (120, 100))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Dino.dinosaur
        self.rect = self.dinosaur.get_rect()
        x, y = 300, 250
        self.rect.x = x
        self.rect.y = y
        self.isJump = False
        self.jumpCount = 10

    def update(self):
        pass
        # if self.isJump and self.rect.y == 0:
        #     if self.jumpCount >= -10:
        #         neg = 1
        #         if self.jumpCount < 0:
        #             neg = -1
        #         self.rect.y -= self.jumpCount ** 2 * 0.1 * neg
        #         self.jumpCount -= 1
        #         self.isJump = False
        #     else:
        #         self.isJump = False
        #         self.jumpCount = 10

