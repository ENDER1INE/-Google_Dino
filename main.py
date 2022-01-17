import pygame
import os
import sys


from dinozavr import Dino
from objects import Stone

SIZE = WIDTH, HEIGHT = 1000, 400
screen = pygame.display.set_mode(SIZE)
running = True
start_flag = False  # <<< Флаг старта движения
isJump = False
boom = False
jumpCount = 10
pos_x = 0  # <<< Позиция старта
speed = 4  # <<< Скорость движения
clock_fps = pygame.time.Clock()
fps = 60
count = 0

stones = pygame.sprite.Group()
Stone(stones)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def time_speed_up():  # <<< функция счета секунд
    return int(pygame.time.get_ticks()) // 1000


dino_sprite = pygame.sprite.Group()
drag = Dino(load_image("dino_anim.png"), 5, 2, 20, 270, dino_sprite)
#  drag_jump = Dino(load_image("1_2_string.png"), 5, 2, 20, 270, dino_sprite)


# <<< background
background_width, background_height = SIZE
background = pygame.transform.smoothscale(load_image('background.png'), (background_width, background_height))
# <<<

pygame.init()
pygame.font.init()

count_score = 10
font_1 = pygame.font.Font(None, 36)

while running:
    if start_flag:
        if count_score % 50 == 0:
            speed += 1
    text1 = font_1.render(str(count_score), True,
                      (255, 255, 255))
    print(speed)
    clock_fps.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Начало движение (SPACE) <<<
    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_SPACE]:
        count_score += 10
        if count >= 1:
            drag.isJump = True
        start_flag = True
        count += 1

    if start_flag:
        pos_x -= speed

    #  Движение заднего фона <<<
    coord_image_1 = pos_x % background_width
    coord_image_2 = coord_image_1 - background_width if coord_image_1 > 0 else coord_image_1 + background_width
    screen.blit(background, (coord_image_1, 0)), screen.blit(background, (coord_image_2, 0))
    # >>>
    dino_sprite.draw(screen)
    stones.draw(screen)

    if start_flag:
        dino_sprite.update()
        stones.update()
    if boom:
        drag.kill()
        screen.blit(game_over, (380, 80))

    screen.blit(text1, (950, 10))
    pygame.display.update()

    drag.jump()

    pygame.display.flip()
pygame.quit()