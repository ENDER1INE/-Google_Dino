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

    def init(self, group):
        super().init(group)
        self.dinosaur = Dino.dinosaur
        self.rect = self.dinosaur.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def update(self):
       pass


pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

bg_w, bg_h = size
bg = pygame.transform.smoothscale(pygame.image.load('background.png'), (bg_w, bg_h))
pos_x = 0
speed = 10
all_sprites = pygame.sprite.Group()
Dino(all_sprites)
all_sprites.draw(screen)

done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_SPACE]:
        pos_x += -speed

    x_rel = pos_x % bg_w
    if x_rel > 0:
        x_part2 = x_rel - bg_w
    else:
        x_part2 = x_rel + bg_w

    screen.blit(bg, (x_rel, 0))
    screen.blit(bg, (x_part2, 0))
    pygame.display.flip()
pygame.quit()