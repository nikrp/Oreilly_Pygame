# Imports
import pygame
import toolbox.event_checker as check_event
import toolbox.rgb_colors as colors
import toolbox.blitter as blitter

# Display Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Initialize Pygame
pygame.init()

# Display Settings
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Text")

# Define Fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('assets/DripOctober.ttf', 32)

# Define Text
system_text, system_text_rect = blitter.blitter_text_center(system_font, "Feed the Dragon", True, colors.GREEN, colors.DARKGREEN, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
custom_text, custom_text_rect = blitter.blitter_text_center(custom_font, "Feed the Dragon", True, colors.GREEN, colors.DARKGREEN, WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)


# Main Loop
running = True
while running:
    running = check_event.quit()

    # Blit the Text Surfaces to the Display Surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    # Update the Display
    pygame.display.update()

# End the Game
pygame.quit()