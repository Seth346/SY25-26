import pygameh
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False

# Function to check for a "near miss"
def is_near_miss(player_pos, player_size, enemy_pos, enemy_size):
    # Check if the enemy is very close to the player but not colliding
    return (abs(player_pos[0] - enemy_pos[0]) < player_size and
            abs(player_pos[1] - enemy_pos[1]) < player_size * 2)
#This will check the play position and the enemy position and will check to see if they are close enough to eneable a near miss
#This will enble the player to double their size.
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # --- Movement Logic ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  # Should move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  # Should move right

    # Keep player within screen bounds
    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # --- Resetting the Enemy ---
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0  # Reset to top
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)  # New random X position
        score += 1
        print(f"Score: {score}")

        # Instead of linear speed increases, fluctuate enemy speed randomly
        enemy_speed = random.randint(5, 15)  # Randomize speed between 5 and 15

        # Grow the player's size slightly as the game progresses
        player_size += 1  # Increase player size by 1 pixel

    # --- Near Miss Effect ---
    if is_near_miss(player_pos, player_size, enemy_pos, enemy_size):
        # Add a brief jitter effect to simulate physical impact
        jitter_x = random.randint(-5, 5)  # Random jitter in X direction
        jitter_y = random.randint(-5, 5)  # Random jitter in Y direction
        screen.scroll(jitter_x, jitter_y)  # Apply the jitter effect to the screen

    # --- Collision Detection ---
    while (enemy_pos[0] < player_pos[0] + player_size and
           enemy_pos[0] + enemy_size > player_pos[0] and
           enemy_pos[1] < player_pos[1] + player_size and
           enemy_pos[1] + enemy_size > player_pos[1]):
        print("Game Over!")
        game_over = True
        break

    # Drawing
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()

