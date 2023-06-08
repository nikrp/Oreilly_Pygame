# Imports
import pygame

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# Initialize Pygame
pygame.init()

# Open a Display Window and Set its Caption
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello World!")

# Create the Main Loop
running = True
while running:
    # Loop Through a List of Event Objects that have Occured
    for event in pygame.event.get():
        # Check if "X" Button is Pressed
        if event.type == pygame.QUIT:
            # Close the Window
            running = False
            
# End the Game
pygame.quit()