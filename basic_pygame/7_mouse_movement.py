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
pygame.display.set_caption("Mouse Movement")

# Load Images
dragon_image_left = pygame.image.load("assets/dragon_left.png")
dragon_image_big = pygame.transform.flip(dragon_image_left, True, False)
dragon_image = pygame.transform.scale(dragon_image_big, (30, 30))
dragon_rect = dragon_image.get_rect()
dragon_rect.x = 25
dragon_rect.y = 25

# Main Loop
running = True
while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # # Move Based on Mouse Clicks
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_x = event.pos[0]
        #     mouse_y = event.pos[1]
        #     dragon_rect.centerx, dragon_rect.centery = mouse_x, mouse_y
        
        # Move Based on Mouse Location
        if event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.x, dragon_rect.centery = 25, mouse_y
    
    if dragon_rect.y > 250:
        dragon_rect.y = 250

    # Fill the Display
    display_surface.fill((0, 0, 0))

    # Blit Assets
    display_surface.blit(dragon_image, dragon_rect)

    # Update the Display
    pygame.display.update()

# End the Game
pygame.quit()