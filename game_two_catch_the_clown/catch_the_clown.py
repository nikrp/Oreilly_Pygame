# Imports
import pygame as pg
import random
import os

# Try the Working Directory
try:
    os.chdir("./game_two_catch_the_clown")
except FileNotFoundError:
    pass

# Initialize Pygame
pg.init()

# Set Display Surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Catch the Clown")
pg.display.set_icon(pg.image.load("clown_icon.png"))

# Set the FPS and Clock
FPS = 60
clock = pg.time.Clock()

# Set Game Values
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = .5

score = 0
player_lives = PLAYER_STARTING_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

# Set Colors
GRAY = (37, 150, 190)
WHITE = (255, 255, 255)

# Set Fonts
font = pg.font.Font("BlackNorth.otf", 32)

# Set Text
title_text = font.render("Catch the Clown", True, GRAY)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render("Score: " + str(score), True, WHITE)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render("Lives: " + str(player_lives), True, WHITE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

game_over_text = font.render("GAMEOVER", True, GRAY, WHITE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Click Anywhere to Play Again", True, WHITE, GRAY)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# Set Sound and Music
click = pg.mixer.Sound("click.mp3")
miss = pg.mixer.Sound("miss.wav")
bg_music = pg.mixer.music.load("bg.mp3")

# Set Images
bg_image_big = pg.image.load("bg.jpg")
bg_image = pg.transform.scale(bg_image_big, (WINDOW_WIDTH, WINDOW_HEIGHT))
bg_rect = bg_image.get_rect()
bg_rect.topleft = (0, 0)

clown_image = pg.image.load("clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Start the Background Music
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play(-1, 0.0)

# The Main Loop
running = True
while running:
    # Check to See if the User Wants to Quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            # The Clown was Clicked
            if clown_rect.collidepoint(mouse_x, mouse_y):
                score += 1
                clown_velocity += CLOWN_ACCELERATION
                click.play()

                # Move the Clown in a new Direction
                previous_dx = clown_dx
                previous_dy = clown_dy
                while (previous_dx == clown_dx and previous_dy == clown_dy):
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])

            # The Click Missed the Clown
            else:
                player_lives -=1
                miss.play()

    # Move the Clown
    clown_rect.x += clown_dx * clown_velocity
    clown_rect.y += clown_dy * clown_velocity

    # Bounce the Clown
    if clown_rect.left <= 0 or clown_rect.right >= WINDOW_WIDTH:
        clown_dx = -1 * clown_dx
    if clown_rect.top <= 0 or clown_rect.bottom >= WINDOW_HEIGHT:
        clown_dy = -1 * clown_dy
    
    # Update HUD
    score_text = font.render("Score: " + str(score), True, WHITE)
    lives_text = font.render("Lives: " + str(player_lives), True, WHITE)

    # Check for Game Over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pg.display.update()

        # Pause the Game until the Player Clicks
        pg.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    is_paused = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES

                    clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                    clown_velocity = CLOWN_STARTING_VELOCITY

                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])

                    pg.mixer.music.play(-1)

                    is_paused = False
    
    # Blit Background
    display_surface.blit(bg_image, bg_rect)

    # Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    # Blit Assets
    display_surface.blit(clown_image, clown_rect)

    # Update the Display and Tick the Clock
    pg.display.update()
    clock.tick(FPS)

# Quit the Game
pg.quit()