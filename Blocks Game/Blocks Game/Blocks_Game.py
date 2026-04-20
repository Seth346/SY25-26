

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False

def is_near_miss(player_pos, player_size, enemy_pos, enemy_size):
    return (abs(player_pos[0] - enemy_pos[0]) < player_size and
            abs(player_pos[1] - enemy_pos[1]) < player_size * 5)
   #near miss
      #This will apply a jitter in the X direction
         #This will apply a jitter in the y direction  # Apply the jitter effect to the screen using the scroll method.
        #The scroll method will move the entire screen by the specified amount, creating a shaking effect that simulates a near miss.
# Load images before the game loop
player_image = pygame.image.load("patrick.jpg")  # Replace with your player image file
player_image = pygame.transform.scale(player_image, (player_size, player_size))  # Scale to player size

enemy_image = pygame.image.load("fireballblock.png")  # Replace with your enemy image file
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))  # Scale to enemy size

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  

    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))

    enemy_pos[1] += enemy_speed

    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0  
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)  
        score += 1
        print(f"Score: {score}")
        enemy_speed = random.randint(5, 15)

    if is_near_miss(player_pos, player_size, enemy_pos, enemy_size):
        jitter_x = random.randint(-5, 5)
        jitter_y = random.randint(-5, 5)
        enemy_pos[0] += jitter_x
        enemy_pos[1] += jitter_y

    while (enemy_pos[0] < player_pos[0] + player_size and
           enemy_pos[0] + enemy_size > player_pos[0] and
           enemy_pos[1] < player_pos[1] + player_size and
           enemy_pos[1] + enemy_size > player_pos[1]):
        print("Game Over!")
        game_over = True
        break

    screen.fill((0, 0, 0))

   
    screen.blit(enemy_image, (enemy_pos[0], enemy_pos[1]))

   
    screen.blit(player_image, (player_pos[0], player_pos[1]))

    pygame.display.update()
    clock.tick(30)

pygame.quit()