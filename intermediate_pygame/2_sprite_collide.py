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

class Player(pygame.sprite.Sprite):
    """A simple class to represent a player who fights monsters."""
    def __init__(self, x, y, monster_group):
        super().__init__()
        self.image = pygame.image.load("muffin.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        self.velocity = 5
        
        self.monster_group = monster_group
    
    def update(self):
        """Update the player"""
        self.move()
        self.check_collisions()
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity
    
    def check_collisions(self):
        if pygame.sprite.spritecollide(self, self.monster_group, True):
            print(len(self.monster_group))

# Create a monster group and add 10 classes
monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i * 64, 10)
    monster_group.add(monster)

# Create a player group and add a player
player_group = pygame.sprite.Group()
player = Player(500, 500, monster_group)
player_group.add(player)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the Display
    display_surface.fill((255, 255, 255))
    
    # Draw Assets and Update Them
    player_group.update()
    player_group.draw(display_surface)
    monster_group.update()
    monster_group.draw(display_surface)
    
    # Update the Display and Tick the Clock
    pygame.display.update()
    clock.tick(FPS)

# End the Game
pygame.quit()