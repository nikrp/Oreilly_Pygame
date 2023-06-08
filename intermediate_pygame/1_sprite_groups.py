# Imports
import pygame, os, random

# Check the Working Directory
try:
    os.chdir("./intermediate_pygame")
except FileNotFoundError:
    pass

# Initialize Pygame
pygame.init()

# Set Display Surface
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sprite Groups")

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

# Define Classes
class Monster(pygame.sprite.Sprite):
    """A simple class to represent a spooky monster."""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)
    
    def update(self):
        """Update and move the monster"""
        self.rect.y += self.velocity

# Create a monster group and add 10 classes
monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i * 64, 10)
    monster_group.add(monster)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the Display
    display_surface.fill((0, 0, 0))
    
    # Draw Assets and Update Them
    monster_group.update()
    monster_group.draw(display_surface)
    
    # Update the Display and Tick the Clock
    pygame.display.update()
    clock.tick(FPS)

# End the Game
pygame.quit()