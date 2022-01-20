import os
import sys

import pygame.mask

from game_parts import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Dino(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, *group):
        super().__init__(*group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.x, self.y = x, y
        self.image = self.frames[self.cur_frame]
        self.rect = pygame.rect.Rect(x + 200, y, 100, 70)
        self.isJump = False
        self.jumpCount = 10
        self.mask = pygame.mask.from_surface(self.image)
        self.start_flag = start_flag

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.image = self.frames[self.cur_frame]
        self.elapsed = pygame.time.get_ticks()
        if self.elapsed % 4 == 0:  # animate every half second
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1.16
                self.rect.y -= self.jumpCount ** 2 * 0.2 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
                self.rect.y = self.y
