import pygame
import random

snake_x = 400
snake_y = 400
snake_width = 5
snake_height = 5

change_x = 0
change_y = 0

food_on_screen = False

red = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1200, 700))

running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, red, (snake_x, snake_y, snake_width, snake_height))
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        change_x = 0
        change_y = -1
    elif keys[pygame.K_DOWN]:
        change_x = 0
        change_y = 1
    elif keys[pygame.K_LEFT]:
        change_x = -1
        change_y = 0
    elif keys[pygame.K_RIGHT]:
        change_x = 1
        change_y = 0

    snake_x += change_x
    snake_y += change_y

    pygame.draw.rect(screen, red, (snake_x, snake_y, snake_width, snake_height))
    pygame.display.update()

    if not food_on_screen:
        food_x = random.randint(1, 1200)
        food_y = random.randint(1, 700)
        food_size = 8
        food_on_screen = True

    pygame.draw.rect(screen, (255, 255, 255), (food_x, food_y, food_size, food_size))

    pygame.display.update()

    if snake_x in range(food_x - food_size, food_x + food_size) and snake_y in range(
        food_y - food_size, food_y + food_size
    ):
        food_on_screen = False


pygame.quit()
