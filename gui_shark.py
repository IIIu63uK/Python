import pygame
import time
import random

# Настройки окна
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Настройки змейки
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [0, 10]
food_pos = [random.randrange(1, WIDTH//10)*10, random.randrange(1, HEIGHT//10)*10]
food_spawn = True
score = 0

# Настройки цветов
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0,255,0)
BLUE = (50, 153, 213)

# Игровой цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(WHITE)

    # Движение змейки
    snake_pos[0][0] += snake_speed[0]
    snake_pos[0][1] += snake_speed[1]

    # Появление еды
    if food_spawn:
        food_pos = [random.randrange(1, WIDTH//10)*10, random.randrange(1, HEIGHT//10)*10]
    food_spawn = False

    # Отрисовка змейки и еды
    for pos in snake_pos:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Проверка на столкновение с едой
    if snake_pos[0] == food_pos:
        score += 1
        food_spawn = True

    pygame.display.update()

pygame.quit()