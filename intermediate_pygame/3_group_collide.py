# Import
import pygame, random, os

# Check the Working Directory
try:
    os.chdir("./intermediate_pygame")
except FileNotFoundError:
    pass

# Initialize Pygame
pygame.init()

# Display Settings
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Group Collide")

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

# Define Classes
class Game():
    """A class to help manage and run our game"""
    def __init__(self, monster_group, knight_group):
        self.monster_group = monster_group
        self.knight_group = knight_group
    
    def update(self):
        self.check_collisions()
    
    def check_collisions(self):
        pygame.sprite.groupcollide(knight_group, monster_group, False, True)

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

class Knight(pygame.sprite.Sprite):
    """A simple class to represent a muffin warrior."""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("muffin.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)
    
    def update(self):
        """Update and move the monster"""
        self.rect.y -= self.velocity

# Make the Sprite Groups
monster_group = pygame.sprite.Group()
for i in range(12):
    monster = Monster(i * 64, 10)
    monster_group.add(monster)
    
knight_group = pygame.sprite.Group()
for i in range(12):
    knight = Knight(i * 64, WINDOW_HEIGHT - 64)
    knight_group.add(knight)
    
# Create a Game Object
game = Game(monster_group, knight_group)

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the Surface
    display_surface.fill((255, 255, 255))
    
    # Update and Draw Sprites
    monster_group.update()
    monster_group.draw(display_surface)
    
    knight_group.update()
    knight_group.draw(display_surface)

    # Update the Game
    game.update()
    
    # Update the Display and Tick the Clock
    pygame.display.update()
    clock.tick(FPS)

# End the Game
pygame.quit()