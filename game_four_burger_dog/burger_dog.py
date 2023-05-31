"""
Author: Nikhil Pellakuru
Date: 5/30/2023
"""

# Imports
import pygame, random, os

# Check the Working Directory
try:
    os.chdir("./game_four_burger_dog")
except FileNotFoundError:
    pass

# Initialize Pygame
pygame.init()

# Display Surface
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
display_surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Burger Dog")

# FPS and Clock
FPS = 60
clock = pygame.time.Clock()

# Set Game Values
PLAYER_STARTING_LIVES = 3
PLAYER_STARTING_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 12
BOOST_CAP = 100
BURGER_POINTS_START = 4000
BUFFER_DISTANCE = -100
BURGER_STARTING_VELOCITY = 3
BURGER_ACCELERATION = .5

player_lives = PLAYER_STARTING_LIVES
player_boost = BOOST_CAP
player_velocity = PLAYER_STARTING_VELOCITY
burger_points = BURGER_POINTS_START
burgers_eaten = 0
burger_velocity = BURGER_STARTING_VELOCITY
score = 0
final_score = score

dog_image_direction = 0 # 0 is Right and 1 is Left
current_dog_image = None

# Set Colors
BLACK = (0, 0, 0)
DARKORANGE = (255, 140, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set Fonts
font = pygame.font.Font("AlleyGarden2.otf", 32)

# Set Text
title_text = font.render("Burger Dog", True, DARKORANGE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_SIZE[0] // 2
title_rect.y = 10

burger_points_text = font.render("Burger Points: " + str(burger_points), True, DARKORANGE)
burger_points_rect = burger_points_text.get_rect()
burger_points_rect.topleft = (10, 10)

score_text = font.render("Score: " + str(score), True, DARKORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 75)

burgers_eaten_text = font.render("Burgers Eaten: " + str(burgers_eaten), True, DARKORANGE)
burgers_eaten_rect = burgers_eaten_text.get_rect()
burgers_eaten_rect.centerx = WINDOW_SIZE[0] // 2
burgers_eaten_rect.y = 75

lives_text = font.render("Lives: " + str(player_lives), True, DARKORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_SIZE[0] - 10, 10)

boost_text = font.render("Boost: " + str(player_boost), True, DARKORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_SIZE[0] - 10, 75)

final_score_text = font.render("Final Score: " + str(final_score), True, DARKORANGE)
final_score_rect = final_score_text.get_rect()
final_score_rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

continue_text = font.render("Press Any Key to Play Again", True, DARKORANGE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 100)

# Set Sounds and Music
bark = pygame.mixer.Sound("bark.mp3")
miss = pygame.mixer.Sound("miss.mp3")

bark.set_volume(3)
miss.set_volume(3)

background_music = pygame.mixer.music.load("background_music.mp3")

# Set Images
dog_left_image = pygame.image.load("dog_left.png")
dog_right_image = pygame.image.load("dog_right.png")
burger_image_big = pygame.image.load("hamburger.png")

burger_image = pygame.transform.scale(burger_image_big, (30, 30))

dog_left_image_rect = dog_left_image.get_rect()
dog_rect = dog_right_image.get_rect()
burger_image_rect = burger_image.get_rect()

dog_rect.centerx = WINDOW_SIZE[0] // 2
dog_rect.y = WINDOW_SIZE[1] - 50

burger_image_rect.x = random.randint(0, WINDOW_SIZE[0] - burger_image.get_width())
burger_image_rect.y = BUFFER_DISTANCE

# Play the Background Music
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# The Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False

    # Remove Burger Points
    if burger_points > 0:
        burger_points -= 7
    
    # Move the Dog
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and dog_rect.left > 0:
        dog_rect.x -= player_velocity
        dog_image_direction = 1
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and dog_rect.right < WINDOW_SIZE[0]:
        dog_rect.x += player_velocity
        dog_image_direction = 0
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and dog_rect.top > 130:
        dog_rect.y -= player_velocity
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and dog_rect.bottom < WINDOW_SIZE[1]:
        dog_rect.y += player_velocity
    
    # Check for Player Boost
    if keys[pygame.K_SPACE] and player_boost > 0:
        player_velocity = PLAYER_BOOST_VELOCITY
        player_boost -= 1
    else:
        player_velocity = PLAYER_STARTING_VELOCITY
    
    # Move the Burger
    burger_image_rect.y += burger_velocity

    # Check for Collisions with the Burger
    if dog_rect.colliderect(burger_image_rect):
        score += burger_points
        burger_points = BURGER_POINTS_START
        burger_velocity += BURGER_ACCELERATION
        burgers_eaten += 1
        if player_boost >= 50 and player_boost < BOOST_CAP:
            player_boost += BOOST_CAP - player_boost
        if player_boost < 50:
            player_boost += 50
        burger_image_rect.x = random.randint(0, WINDOW_SIZE[0] - burger_image.get_width())
        burger_image_rect.y = BUFFER_DISTANCE
        bark.play()
    
    # Check if the Player Misses a Burger
    if burger_image_rect.top > WINDOW_SIZE[1]:
        player_lives -= 1
        burger_velocity = BURGER_STARTING_VELOCITY
        burger_points = BURGER_POINTS_START
        dog_rect.centerx = WINDOW_SIZE[0] // 2
        dog_rect.y = WINDOW_SIZE[1] - 50
        burger_image_rect.x = random.randint(0, WINDOW_SIZE[0] - burger_image.get_width())
        burger_image_rect.y = BUFFER_DISTANCE
        miss.play()

    # Make the Current Dog Image One of the Dog Images
    if dog_image_direction == 0:
        current_dog_image = dog_right_image
    else:
        current_dog_image = dog_left_image

    # Update the HUD
    title_text = font.render("Burger Dog", True, DARKORANGE)
    burger_points_text = font.render("Burger Points: " + str(burger_points), True, DARKORANGE)
    burgers_eaten_text = font.render("Burgers Eaten: " + str(burgers_eaten), True, DARKORANGE)
    score_text = font.render("Score: " + str(score), True, DARKORANGE)
    lives_text = font.render("Lives: " + str(player_lives), True, DARKORANGE)
    boost_text = font.render("Boost: " + str(player_boost), True, DARKORANGE)

    # Check for a Death
    if player_lives == 0:
        final_score = score
        pygame.mixer.music.fadeout(50)
        paused = True
        final_score_text = font.render("Final Score: " + str(final_score), True, DARKORANGE)
        display_surface.blit(final_score_text, final_score_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    score = 0
                    burger_points = BURGER_POINTS_START
                    player_lives = PLAYER_STARTING_LIVES
                    burger_velocity = BURGER_STARTING_VELOCITY
                    burgers_eaten = 0
                    player_boost = BOOST_CAP
                    paused = False
                    pygame.mixer.music.play()
    
    # Fill the Display
    display_surface.fill(BLACK)

    # Blit the HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(burger_points_text, burger_points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(burgers_eaten_text, burgers_eaten_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)
    pygame.draw.line(display_surface, WHITE, (0, 130), (WINDOW_SIZE[0], 130), 3)

    # Blit Assets
    display_surface.blit(current_dog_image, dog_rect)
    display_surface.blit(burger_image, burger_image_rect)
    
    # Update the Display and Tick the Clock
    pygame.display.update()
    clock.tick(FPS)

# Quit the Game
pygame.quit()