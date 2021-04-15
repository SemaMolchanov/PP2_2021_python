import pygame
import random
import time

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('SNAKE GAME')

THE_END = False

clock = pygame.time.Clock()

while not THE_END:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            THE_END = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                THE_END = True

    pygame.display.flip()
