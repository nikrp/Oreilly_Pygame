# Import Pygame
import pygame

# Initialize Pygame
pygame.init()

def quit():
    # Loop Through a List of Event Objects that have Occured
    for event in pygame.event.get():
        # Check if "X" Button is Pressed
        if event.type == pygame.QUIT:
            # Close the Window
            return False
    return True

def mouse_down(*args):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            args[0] = mouse_x
            args[1] = mouse_y
            return True, args[0], args[1]
    return False, None, None

# End the Game
pygame.quit()