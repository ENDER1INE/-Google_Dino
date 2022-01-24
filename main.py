import os
import random
import sys

import pygame.transform

from objects import Stone, Cactus
from dinozavr import Dino
from game_parts import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def time_speed_up():  # <<< функция счета секунд
    return pygame.time.get_ticks() // 1000


class StartScreen(pygame.sprite.Sprite):
    start_screen_image = pygame.transform.scale(load_image("start_screen.png"), (1000, 400))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = StartScreen.start_screen_image
        self.rect = pygame.rect.Rect(0, 0, 1000, 400)


objects = pygame.sprite.Group()
start_screen_sprite = pygame.sprite.Group()
StartScreen(start_screen_sprite)
stone = Stone(objects)
cactus = Cactus(objects)


dino_sprite = pygame.sprite.Group()
drag = Dino(load_image("dino_anim.png"), 5, 2, 20, 270, dino_sprite)


# <<< background
background_width, background_height = SIZE
background = pygame.transform.smoothscale(load_image('background.png'), (background_width, background_height))
# <<<

pygame.init()
pygame.font.init()

font_1 = pygame.font.Font(None, 36)
font_2 = pygame.font.Font(None, 50)
text1 = font_1.render(str(count_score), True,
                          (255, 255, 255))
text2 = font_2.render(str(count_score), True,
                          (0, 0, 0))
text3 = font_2.render(str(max(counts_records)), True,
                              (0, 0, 0))
text4 = font_1.render('Name:', True,
                              (0, 0, 0))
input_box = pygame.Rect(760, 50, 140, 32)
f = open('records.txt', mode='w', encoding='utf8')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEOEXPOSE:
            start_flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    f = open('records.txt', mode='w', encoding='utf8')
                    print(f'{text}: {count_score - 10}', file=f)
                    text = ''
                    active = False
                    color = color_inactive
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
    if start_flag:
        if count_score % 50 == 0:
            speed += 1
            Stone.speed_object += 1
            Cactus.speed_object += 1
            count_score += 10
        text1 = font_1.render(str(count_score - 10), True,
                              (255, 255, 255))
        text2 = font_2.render(str(count_score - 10), True,
                              (0, 0, 0))
    clock_fps.tick(40)

    # Начало движение (SPACE) <<<

    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_SPACE]:
        if count >= 1:
            drag.isJump = True
        start_flag = True
        count += 1

    if time_speed_up() not in list_second:
        list_second.append(time_speed_up())

    if start_flag:
        if not game_over:
            pos_x -= speed

    if len(list_second) % 5 == 0:
        count_score += 10
        list_second.append('space')
        Cactus(objects) if random.randint(1, 2) == 1 else Stone(objects)


    #  Движение заднего фона <<<
    coord_image_1 = pos_x % background_width
    coord_image_2 = coord_image_1 - background_width if coord_image_1 > 0 else coord_image_1 + background_width
    screen.blit(background, (coord_image_1, 0)), screen.blit(background, (coord_image_2, 0))
    # >>>
    dino_sprite.draw(screen)
    objects.draw(screen)

    if Stone.contact:
        start_flag = False
        boom = True
        again = True
        game_over = True

    if start_screen_flag:
        start_screen_sprite.draw(screen)

    if game_over:
        if allKeys[pygame.K_SPACE]:
            pygame.time.delay(500)
            counts_records.append(count_score - 10)
            objects.remove(objects)
            pos_x = 0
            game_over = False
            Stone.contact = False
            start_flag = True
            boom = False
            count_score = 10
            list_second.clear()
            speed = 9
            Stone.speed_object = 9
            Cactus.speed_object = 9
            start_screen_flag = True

    if start_flag:
        start_screen_flag = False
        dino_sprite.update()
        objects.update()
        drag.jump()

    if pygame.sprite.spritecollideany(drag, objects):
        Stone.contact = True

    if boom:
        start_flag = False
        end_game_page = load_image('go.png')
        score = load_image('score.png')
        best_sc = load_image('kubok.png')
        peso = load_image('PESO.png')
        score = pygame.transform.scale(score, (100, 100))
        end_game_page = pygame.transform.scale(end_game_page, (300, 150))
        screen.blit(end_game_page, (350, 50))
        screen.blit(score, (420, 200))
        screen.blit(text2, (530, 227))
        screen.blit(best_sc, (420, 260))
        screen.blit(peso, (300, 360))
        text3 = font_2.render(str(max(counts_records)), True,
                              (0, 0, 0))
        screen.blit(text3, (530, 264))
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(text4, (680, 55))
        txt = font_1.render(text, True, 'black')
        input_box.w = max(200, txt.get_width() + 10)
        screen.blit(txt, (input_box.x + 5, input_box.y + 5))
    if not start_screen_flag:
        screen.blit(text1, (950, 10))
    screen.blit(text1, (950, 10))
    pygame.display.update()
    pygame.display.flip()
pygame.quit()