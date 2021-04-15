import pygame
import random
import time


pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('SNAKE GAME')

THE_END = False

displacement = 5
radius = 5
#i = 1

clock = pygame.time.Clock()

class Snake:
    def __init__(self, x , y):
        self.blocks = [[x, y]]
        self.size = 1
        self.displacementX = displacement
        self.displacementY = 0
        self.is_growing = False
        self.radius = radius
        self.direction = 'right'

    def draw(self, tail_color):
        pygame.draw.circle(screen, YELLOW, (self.blocks[0][0], self.blocks[0][1]), self.radius)
        for block in self.blocks[1:]:
                pygame.draw.circle(screen, tail_color, block, self.radius)
        

    def add_block(self):
        self.size += 1
        self.blocks.insert(0, [self.blocks[0][0] + self.displacementX, self.blocks[0][1] + self.displacementY])
        self.is_growing = False

    def move(self):
        global THE_END

        if self.is_growing:
            self.add_block()

        for j in range(self.size - 1, 0, -1):
            self.blocks[j][0] = self.blocks[j - 1][0]
            self.blocks[j][1] = self.blocks[j - 1][1]

        self.blocks[0][0] += self.displacementX
        self.blocks[0][1] += self.displacementY

        if self.blocks[0] in self.blocks[1:]:
            THE_END = True

#class Apple(self):
   # self.radius = radius

snake1 = Snake(100, 100)
snake2 = Snake(700, 500)

while not THE_END:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            THE_END = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                THE_END = True
            elif event.key == pygame.K_DOWN and snake1.direction != 'up':
                snake1.displacementX = 0
                snake1.displacementY = displacement
                snake1.direction = 'down'
            elif event.key == pygame.K_UP and snake1.direction != 'down':
                snake1.displacementX = 0
                snake1.displacementY = -displacement
                snake1.direction = 'up'
            elif event.key == pygame.K_LEFT and snake1.direction != 'right':
                snake1.displacementX = -displacement
                snake1.displacementY = 0
                snake1.direction = 'left'
            elif event.key == pygame.K_RIGHT and snake1.direction != 'left':
                snake1.displacementX = displacement
                snake1.displacementY = 0
                snake1.direction = 'right'
            elif event.key == pygame.K_s and snake2.direction != 'up':
                snake2.displacementX = 0
                snake2.displacementY = displacement
                snake2.direction = 'down'
            elif event.key == pygame.K_w and snake2.direction != 'down':
                snake2.displacementX = 0
                snake2.displacementY = -displacement
                snake2.direction = 'up'
            elif event.key == pygame.K_a and snake2.direction != 'right':
                snake2.displacementX = -displacement
                snake2.displacementY = 0
                snake2.direction = 'left'
            elif event.key == pygame.K_d and snake2.direction != 'left':
                snake2.displacementX = displacement
                snake2.displacementY = 0
                snake2.direction = 'right'
            elif event.key == pygame.K_1:
                snake1.is_growing = True
            elif event.key == pygame.K_2:
                snake2.is_growing = True

    if snake1.blocks[0][0] < 0:
        snake1.blocks[0][0] = SCREEN_WIDTH
    if snake1.blocks[0][0] > SCREEN_WIDTH:
        snake1.blocks[0][0] = 0
    if snake1.blocks[0][1] < 0:
        snake1.blocks[0][1] = SCREEN_HEIGHT
    if snake1.blocks[0][1] > SCREEN_HEIGHT:
        snake1.blocks[0][1] = 0
    if snake2.blocks[0][0] < 0:
        snake2.blocks[0][0] = SCREEN_WIDTH
    if snake2.blocks[0][0] > SCREEN_WIDTH:
        snake2.blocks[0][0] = 0
    if snake2.blocks[0][1] < 0:
        snake2.blocks[0][1] = SCREEN_HEIGHT
    if snake2.blocks[0][1] > SCREEN_HEIGHT:
        snake2.blocks[0][1] = 0



    if snake1.blocks[0] in snake2.blocks[:] or snake2.blocks[0] in snake1.blocks[:]:
        THE_END = True
    
    snake1.move()
    screen.fill(BLACK)
    snake2.move()
    screen.fill(BLACK)
    snake1.draw(BLUE)
    snake2.draw(RED)
    pygame.display.flip()
