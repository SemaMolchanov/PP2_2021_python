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
i = 1

clock = pygame.time.Clock()

class Snake1:

    '''у змейки есть:
    -блоки (круглешки или квадратики) а именно:
        -голова
        -тело (хвост)
    -размер (кол-во блоков включая голову)
    -направление движения
    -состояние (растет или нет)
    -возможность перемещения по вертикали
    -возможность перемещения по горизонтали'''

    def __init__(self):
        self.blocks = [[100, 100]]
        self.size = 1
        self.displacementX = displacement
        self.displacementY = 0
        self.is_growing = False
        self.radius = radius
        self.direction = 'right'

    #рисуется полосатое тело и отдельным цветом (белым) голова

    def draw(self):
        global i
        pygame.draw.circle(screen, WHITE, (self.blocks[0][0], self.blocks[0][1]), self.radius)
        for block in self.blocks[1:]:
            if i % 2 == 0:
                 pygame.draw.circle(screen, YELLOW, block, self.radius)
            elif i % 2 != 0:
                pygame.draw.circle(screen, BLUE, block, self.radius)
            i += 1
        

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

class Snake2:

    '''у змейки есть:
    -блоки (круглешки или квадратики) а именно:
        -голова
        -тело (хвост)
    -размер (кол-во блоков включая голову)
    -направление движения
    -состояние (растет или нет)
    -возможность перемещения по вертикали
    -возможность перемещения по горизонтали'''

    def __init__(self):
        self.blocks = [[700, 500]]
        self.size = 1
        self.displacementX = -displacement
        self.displacementY = 0
        self.is_growing = False
        self.radius = radius
        self.direction = 'left'

    #рисуется полосатое тело и отдельным цветом (белым) голова

    def draw(self):
        global i
        pygame.draw.circle(screen, WHITE, (self.blocks[0][0], self.blocks[0][1]), self.radius)
        for block in self.blocks[1:]:
            if i % 2 == 0:
                 pygame.draw.circle(screen, YELLOW, block, self.radius)
            elif i % 2 != 0:
                pygame.draw.circle(screen, RED, block, self.radius)
            i += 1
        

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


snake1 = Snake1()
snake2 = Snake2()

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
    
    #snake1.move()
    #screen.fill(BLACK)
    snake2.move()
    screen.fill(BLACK)
    #snake1.draw()
    snake2.draw()
    pygame.display.flip()
