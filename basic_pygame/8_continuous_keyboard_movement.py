# Imports
import pygame

# Initialize Pygame
pygame.init()

# Create a Display Surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Continuous Movement")

# Create a Clock
FPS = 60
clock = pygame.time.Clock()

# Set Game Values
VELOCITY = 5

# Load Images
dragon_image_l = pygame.image.load("feed_the_dragon/dragon_left.png")
dragon_image_r_big = pygame.transform.flip(dragon_image_l, True, False)
dragon_image_right = pygame.transform.scale(dragon_image_r_big, (50, 50))
dragon_rect = dragon_image_right.get_rect()
dragon_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)


# The Main Game Loop
running = True
while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get a List of all Keys Currently Being Pressed Down
    keys = pygame.key.get_pressed()
    
    # Move the Dragon Continuously
    if keys[pygame.K_LEFT]:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_UP]:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN]:
        dragon_rect.y += VELOCITY
    
    # Fill the Display
    display_surface.fill((0, 0, 0))

    # Blit the Dragon Image
    display_surface.blit(dragon_image_right, dragon_rect)
    
    # Update the Display
    pygame.display.update()

    # Tick the Clock
    clock.tick(FPS)

# Quit the Game
pygame.quit()