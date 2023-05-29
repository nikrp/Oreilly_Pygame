# Imports
import pygame
from toolbox.event_checker import quit_checker
from toolbox.rgb_colors import BLUE, RED, GREEN, WHITE, YELLOW, CYAN, MAGENTA

# Window Size Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Initialize Pygame
pygame.init()

# Display Settings
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")
display_surface.fill(BLUE)

# Lines
pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
pygame.draw.line(display_surface, GREEN, (100, 100), (200, 300), 5)

# Circle
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 200, 6)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 195, 0)

# Rectangle
pygame.draw.rect(display_surface, CYAN, (700, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (750, 100, 50, 100))

# Main Loop
running = True
while running:
    # Check the QUIT Event
    running = quit_checker(pygame.QUIT, running)
    
    # Updates
    pygame.display.update()

# End the Game
pygame.quit()