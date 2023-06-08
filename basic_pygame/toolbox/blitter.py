# Import Pygame
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

def blitter_img(img_path, x_coord, y_coord):
    img = pygame.image.load(img_path)
    img_rect = img.get_rect()
    img_rect.x, img_rect.y = x_coord, y_coord
    return img, img_rect

def blitter_img_flip(original_image, x_flip:bool, y_flip:bool, x_coord, y_coord):
    img = pygame.transform.flip(original_image.copy(), x_flip, y_flip)
    img_rect = img.get_rect()
    img_rect.x, img_rect.y = x_coord, y_coord
    return img, img_rect

def blitter_text_center(font, words, alias, primary_color, secondary_color, x_coord, y_coord):
    text = font.render(words, alias, primary_color, secondary_color)
    text_rect = text.get_rect()
    text_rect.center = (x_coord, y_coord)
    return text, text_rect

# End the Game
pygame.quit()