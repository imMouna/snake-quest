import pygame
import random
import math
import time

pygame.init()

# snake size and movement
snake_size = 15

# food properties
food_radius = 5

# setting up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
red_color = (255, 0, 0)
black_color = (0, 0, 0)
green_color = (0, 255, 0)

game_over = False
score = 0

# snake starting positions
x1 = window_width // 2
y1 = window_height // 2

x1_change = 0
y1_change = 0

snake_body = []
# initial length of the snake
length_of_snake = 1

# randomly generate initial food positions
food_x = random.randint(0, (window_width // snake_size) - 1) * snake_size
food_y = random.randint(0, (window_height // snake_size) - 1) * snake_size

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # check for arrow keys pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -15
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 15
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -15
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 15

    x1 = x1 + x1_change
    y1 = y1 + y1_change

    # boundary condition
    if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
        game_over = True

    # clear the screen before drawing the snake
    window.fill(black_color)

    font_style = pygame.font.SysFont(None, 40)
    score_text = font_style.render("Score: " + str(score), True, red_color)
    window.blit(score_text, (10, 10))

    snake_head = [x1, y1]
    snake_body.append(snake_head)

    if len(snake_body) > length_of_snake:
        del snake_body[0]

    # snake collision with itself
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_finished = font_style.render("Game Over", True, red_color)
            window.blit(game_finished, (window_width // 2 - 100, window_height // 2))
            pygame.display.update()  # Ensure the message is displayed
            pygame.time.wait(3000)
            game_over = True

    # check if snake is in contact with food
    distance = math.sqrt((x1 - food_x) ** 2 + (y1 - food_y) ** 2)
    if distance < food_radius + (snake_size // 2):
        # generate new food position
        food_x = random.randint(0, (window_width // snake_size) - 1) * snake_size
        food_y = random.randint(0, (window_height // snake_size) - 1) * snake_size
        length_of_snake += 1
        score += 1

    # draw the snake
    for segment in snake_body:
        pygame.draw.rect(surface=window, color=red_color, rect=[segment[0], segment[1], snake_size, snake_size])

    # draw the food
    pygame.draw.circle(surface=window, color=green_color, center=(food_x, food_y), radius=food_radius)

    pygame.display.update()
    clock.tick(25)

pygame.quit()
