# Imports
import pygame
import random
import os

# Check the Working Directory
try:
    os.chdir("./game_three_snake")
except FileNotFoundError:
    pass

# Initialize Pygame
pygame.init()

# Display Settings
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Snake~~")
pygame.display.set_icon(pygame.image.load("snake_icon.png"))

# Set FPS and Clock
FPS = 20
clock = pygame.time.Clock()

# Set Game Values
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2 + 100

snake_dx = 0
snake_dy = 0

score = 0

# Set Colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

# Set Fonts
font = pygame.font.SysFont("gabriola", 48)

# Set Text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, RED, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any Key to Play Again", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# Set Sounds and Music
crunch = pygame.mixer.Sound("bite.mp3")

# Set Images (In this Game use Simmple Rects...So just Create their Coordinates)
# For a Rectangle you Need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

body_coords = []

# The Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Move the Snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dx != SNAKE_SIZE:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT and snake_dx != -SNAKE_SIZE:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP and snake_dy != SNAKE_SIZE:
                snake_dx = 0
                snake_dy = -SNAKE_SIZE
            if event.key == pygame.K_DOWN and snake_dy != -SNAKE_SIZE:
                snake_dx = 0
                snake_dy = SNAKE_SIZE
    
    # Update the x and y Position of the Snakes Head and Make a New Coordinate
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
    
    # Check for Collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        crunch.play()
        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
    
    # Update HUD
    score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)
            
    # Fill the Display
    display_surface.fill(WHITE)
    
    # Blit the HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    # Blit Assets
    # Still need to do the Body
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

    # Update the Display and Tick the Clock
    pygame.display.update()
    clock.tick(FPS)

# End the Game
pygame.quit()