import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 1200, 768
FPS = 60

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простая игра")

# Создание игрока
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10

# Создание противников
enemy_size = 50
enemies = []

# Создание часов
clock = pygame.time.Clock()


# Функция для создания противников
def create_enemy():
    enemy_x = random.randint(0, WIDTH - enemy_size)
    enemy_y = random.randint(-50, -10)
    enemies.append([enemy_x, enemy_y])


# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка движения игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += 5

    # Обновление координат противников
    for enemy in enemies:
        enemy[1] += 5

        # Проверка столкновения с игроком
        if (
                player_x < enemy[0] < player_x + player_size
                and player_y < enemy[1] < player_y + player_size
        ):
            pygame.quit()
            sys.exit()

        # Удаление противников, вышедших за пределы экрана
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
            create_enemy()

    # Создание новых противников
    if random.randint(1, 20) == 1:
        create_enemy()

    # Очистка экрана
    screen.fill(WHITE)

    # Отрисовка игрока
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Отрисовка противников
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Обновление экрана
    pygame.display.flip()

    # Задержка для поддержания FPS
    clock.tick(FPS)
