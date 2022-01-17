import pygame
import os
import sys

from dinozavr import Dino

SIZE = WIDTH, HEIGHT = 1000, 400
screen = pygame.display.set_mode(SIZE)
speed = 4


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
    stone = pygame.transform.scale(stone, (40, 40))
    spawn_stone = False

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Stone.stone
        self.rect = self.stone.get_rect()
        x, y = 1000, 305
        self.rect.x, self.rect.y = x, y
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        dino = Dino(load_image("dino_anim.png"), 5, 2, 20, 300)
        self.rect = self.rect.move(-5, 0)
        if pygame.sprite.collide_mask(self, dino):
            print('end game')
            start_flag = False
            boom = True
            game_over = pygame.transform.scale(load_image('go.png'), (200, 100))
            screen.blit(game_over, (380, 80))

        if self.rect.right < 0:
            self.kill()