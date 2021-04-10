import pygame
import math
import random

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]

screen = pygame.display.set_mode([800, 600])
screen.fill(BLACK)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and key.type == pygame.K_ESCAPE:
            done = True
    
    pygame.display.flip()