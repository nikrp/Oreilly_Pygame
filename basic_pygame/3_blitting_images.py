# Imports
import pygame
from pygame.locals import *
import toolbox.event_checker as check_event
import toolbox.rgb_colors as colors
import toolbox.blitter as load_image

# Display Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Initialize Pygame
pygame.init()

# Display Settings
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images")

# Create Images - Returns a Surface Object with the Image Drawm on it
# Then we get the Rect of the Surface and Use the Rect to Position the Image
dragon_left_image, dragon_left_rect = load_image.blitter_img("assets/dragon_left.png", 0, 0)
dragon_right_image, dragon_right_rect = load_image.blitter_img_flip(dragon_left_image, True, False, WINDOW_WIDTH - dragon_left_image.get_width(), 0)

print(dragon_left_image.get_height())
# Main Loop
running = True
while running:
    running = check_event.quit(pygame.QUIT)
    
    # Blit a Surface Object at the Given Coordinates
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    
    # Draw a Horizontal Line Under the Dragons
    pygame.draw.line(display_surface, colors.WHITE, (0, dragon_left_image.get_height() + 5), (WINDOW_WIDTH, dragon_left_image.get_height() + 5), 5)
    
    # Updates
    pygame.display.update()

# End the Game
pygame.quit()