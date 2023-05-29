# Imports
import pygame
import toolbox.event_checker as check_event
import toolbox.rgb_colors as colors
import toolbox.blitter as blitter

# Display Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# Initialize Pygame
pygame.init()

# Display Settings
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Keyboard Movements")

# Set Game Values
VELOCITY = 10

# Load in Images
dragon_image = pygame.image.load("assets/dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH // 2
dragon_rect.bottom = WINDOW_HEIGHT

# Main Loop
running = True
while running:
    # Check for Discrete Movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY
            

    display_surface.fill((0, 0, 0))            

    # Blit assets to the Screen
    display_surface.blit(dragon_image, dragon_rect)

    # Update the Display
    pygame.display.update()

# End the Game
pygame.quit()