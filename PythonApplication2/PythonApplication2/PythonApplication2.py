import pygame
import math

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Z-Ball")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

# Load the background image
background = pygame.image.load("assets/videogamebackround.jpg")

# Scale the image to fit the screen dimensions
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Ball
ball_radius = 15  # Define ball_radius before it is used
original_pos = [150, 450]  # Store the original position
ball_pos = original_pos[:]
ball_vel = [0, 0]
ball_grabbed = False
ball_in_motion = False

# Load the ball image
ball_image = pygame.image.load("assets/fireball2.png")
ball_image = pygame.transform.scale(ball_image, (ball_radius * 2, ball_radius * 2))  # Scale to match ball size

# Game clock
clock = pygame.time.Clock()

# Hole
hole_radius = 25
hole_pos = [650, 200]
hole_vel = 2  # Velocity for the hole's vertical movement

# Physics
gravity = 1.0
friction = 0.99

# Score
score = 0  # Initialize the score

running = True
while running:
    clock.tick(60)
    # Draw the background image
    screen.blit(background, (0, 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start aiming
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - ball_pos[0]
            dy = mouse_y - ball_pos[1]
            dist = math.hypot(dx, dy)
            if dist <= ball_radius:
                ball_grabbed = True

        # Release the ball
        elif event.type == pygame.MOUSEBUTTONUP and ball_grabbed:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            ball_vel[0] = (ball_pos[0] - mouse_x) / 10
            ball_vel[1] = (ball_pos[1] - mouse_y) / 10
            ball_in_motion = True
            ball_grabbed = False

    # Dragging ball
    if ball_grabbed:
        # Draw the slingshot line but keep the ball in its original position
        pygame.draw.line(screen, BLACK, (original_pos[0], original_pos[1]), pygame.mouse.get_pos(), 2)

    # Move ball with physics
    if ball_in_motion:
        ball_vel[1] += gravity
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
        ball_vel[0] *= friction
        ball_vel[1] *= friction

        # Collision with walls
        if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > WIDTH or ball_pos[1] + ball_radius > HEIGHT:
            # Teleport the ball back to its original position
            ball_pos = original_pos[:]
            ball_vel = [0, 0]
            ball_in_motion = False

        # Check if ball has stopped moving
        if abs(ball_vel[0]) < 0.1 and abs(ball_vel[1]) < 0.1:
            ball_vel = [0, 0]
            ball_in_motion = False

    # Move the hole up and down
    hole_pos[1] += hole_vel
    if hole_pos[1] - hole_radius < 0 or hole_pos[1] + hole_radius > HEIGHT:
        hole_vel *= -1  # Reverse direction when hitting the top or bottom

    # Check win or collision with the hole
    dx = ball_pos[0] - hole_pos[0]
    dy = ball_pos[1] - hole_pos[1]
    dist_to_hole = math.hypot(dx, dy)
    if dist_to_hole <= hole_radius + ball_radius:  # Stop if the ball touches the hole
        # Increment the score
        score += 1

        # Reset the ball to its original position
        ball_pos = original_pos[:]
        ball_vel = [0, 0]
        ball_in_motion = False

    # Draw hole
    pygame.draw.circle(screen, GRAY, hole_pos, hole_radius)

    # Draw ball
    screen.blit(ball_image, (int(ball_pos[0] - ball_radius), int(ball_pos[1] - ball_radius)))

    # Display the score
    font = pygame.font.SysFont(None, 40)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))  # Draw the score at the top-left corner

    pygame.display.flip()

pygame.quit()
