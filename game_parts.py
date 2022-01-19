import pygame


SIZE = WIDTH, HEIGHT = 1000, 400
screen = pygame.display.set_mode(SIZE)
running = True
start_flag = False  # <<< Флаг старта движения
isJump = False
again = False
boom = False
jumpCount = 10
pos_x = 0  # <<< Позиция старта
speed = 9  # <<< Скорость движения
clock_fps = pygame.time.Clock()
fps = 60
count = 0
count_score = 10
list_second = []