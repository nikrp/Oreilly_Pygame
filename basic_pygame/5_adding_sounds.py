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
pygame.display.set_caption("Sounds Effects")

# Load Sound Effects
sound = pygame.mixer.Sound('assets/sound.wav')
zap = pygame.mixer.Sound('assets/zap.wav')

# Play the Starting Sound Effect
sound.play()

# Load the Background Music and Play it
pygame.mixer.music.load('assets/song.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.3)

# Main Loop
running = True
while running:
    running = check_event.quit()

# End the Game
pygame.quit()