import pygame
import os
import random

# Change the Directory
try:
    os.chdir("./basic_pygame")
except FileNotFoundError:
    pass

# Initialize Pygame
pygame.init()

# Clock and FPS
FPS = 60
clock = pygame.time.Clock()

# Display Surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection")

# Game Values
VELOCITY = 5

# Load Images
dragon_pre_image = pygame.image.load("feed_the_dragon/dragon_left.png")
dragon_big_right = pygame.transform.flip(dragon_pre_image, True, False)
dragon_right = pygame.transform.scale(dragon_big_right, (50, 50))
dragon_rect = dragon_right.get_rect()
dragon_rect.topleft = (25, 25)

pre_coin = pygame.image.load("feed_the_dragon/coin.png")
coin = pygame.transform.scale(pre_coin, (32, 32))
coin_rect = coin.get_rect()
coin_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Continuous Arrow Key Pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_UP] and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY

    # Check for Collision between two Rects
    if dragon_rect.colliderect(coin_rect):
        coin_rect.x = random.randint(0, WINDOW_WIDTH - coin.get_width())
        coin_rect.y = random.randint(0, WINDOW_HEIGHT - coin.get_height())

    # Fill Display Surface
    display_surface.fill((0, 0, 0))

    # Draw Rectangles to See Hitboxes
    pygame.draw.rect(display_surface, (0, 255, 0), dragon_rect, 1)
    pygame.draw.rect(display_surface, (255, 255, 0), coin_rect, 1)

    # Blit Assets
    display_surface.blit(dragon_right, dragon_rect)
    display_surface.blit(coin, coin_rect)
    
    # Update the Display
    pygame.display.update()

    # Tick the Clock
    clock.tick(FPS)

# Quit the Game
pygame.quit()