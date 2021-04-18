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
LIGHT_BROWN = [205, 133, 63]

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

GAMEZONE_WIDTH = 1020
GAMEZONE_HEIGHT = 660

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
#screen.fill(LIGHT_BROWN)
pygame.display.set_caption('SNAKE GAME')

gamezone = pygame.Surface([GAMEZONE_WIDTH, GAMEZONE_HEIGHT])

font = pygame.font.SysFont("Verdana", 60)
game_over_sign = font.render("Game Over", True, BLACK)

font_small = pygame.font.SysFont("Verdana", 20)
red_score = font_small.render('RED SCORE:', True, BLACK)
blue_score = font_small.render('BLUE SCORE:', True, BLACK)



font_small = pygame.font.SysFont("Verdana", 20)

#pygame.draw.rect(screen, BLACK, [30, 30, 1020, 660], 0)

THE_END = False

SPEED = 4
radius = 10
#i = 1

clock = pygame.time.Clock()

'''def game_over():
    time.sleep(1)
    gamezone.fill(RED)
    gamezone.blit(game_over_sign, (30,250))
    pygame.display.update()
    time.sleep(2)
    THE_END = True'''

class Apple:
    def __init__(self):
        self.radius = radius
        self.color = GREEN
        self.x = random.randint((SCREEN_WIDTH - GAMEZONE_WIDTH) + radius, GAMEZONE_WIDTH - radius)
        self.y = random.randint((SCREEN_HEIGHT- GAMEZONE_HEIGHT) + radius, GAMEZONE_HEIGHT - radius)

    def create(self):
        self.x = random.randint((SCREEN_WIDTH - GAMEZONE_WIDTH) + radius, GAMEZONE_WIDTH - radius)
        self.y = random.randint((SCREEN_HEIGHT- GAMEZONE_HEIGHT) + radius, GAMEZONE_HEIGHT - radius)

    def draw(self):
        pygame.draw.circle(gamezone, GREEN, (self.x, self.y), self.radius)

class Snake:
    def __init__(self, x , y):
        self.speed = SPEED
        self.blocks = [[x, y]]
        self.size = 1
        self.dx = self.speed
        self.dy = 0
        self.is_growing = False
        self.radius = radius
        self.direction = 'right'
        self.score = 0

    def draw(self, tail_color):
        pygame.draw.circle(gamezone, tail_color, (self.blocks[0][0], self.blocks[0][1]), self.radius)
        for block in self.blocks[1:]:
                pygame.draw.circle(gamezone, tail_color, block, self.radius)
        

    def add_block(self):
        self.size += 1
        #self.blocks.insert(0, [self.blocks[0][0] + self.displacementX, self.blocks[0][1] + self.displacementY])
        self.blocks.append([0, 0])
        self.is_growing = False

    def move(self):
        global THE_END

        if self.is_growing:
            self.add_block()

        for j in range(self.size - 1, 0, -1):
            self.blocks[j][0] = self.blocks[j - 1][0]
            self.blocks[j][1] = self.blocks[j - 1][1]

        self.blocks[0][0] += self.dx
        self.blocks[0][1] += self.dy

        if self.blocks[0] in self.blocks[1:]:
            #game_over()
            THE_END = True

    def eat(self, apple):
        for i in range(self.size):
            if(abs(self.blocks[i][0] - apple.x) <= apple.radius + self.radius and abs(self.blocks[i][1] - apple.y) <= apple.radius + self.radius):
                return True
        return False



snake1 = Snake(100, 100)
snake2 = Snake(700, 500)
apple = Apple()

while not THE_END:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            THE_END = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                THE_END = True
            elif event.key == pygame.K_DOWN and snake1.direction != 'up':
                snake1.dx = 0
                snake1.dy = snake1.speed #SPEED
                snake1.direction = 'down'
            elif event.key == pygame.K_UP and snake1.direction != 'down':
                snake1.dx = 0
                snake1.dy = -snake1.speed #SPEED
                snake1.direction = 'up'
            elif event.key == pygame.K_LEFT and snake1.direction != 'right':
                snake1.dx= -snake1.speed #SPEED
                snake1.dy = 0
                snake1.direction = 'left'
            elif event.key == pygame.K_RIGHT and snake1.direction != 'left':
                snake1.dx = snake1.speed #SPEED
                snake1.dy = 0
                snake1.direction = 'right'
            elif event.key == pygame.K_s and snake2.direction != 'up':
                snake2.dx = 0
                snake2.dy = snake2.speed #SPEED
                snake2.direction = 'down'
            elif event.key == pygame.K_w and snake2.direction != 'down':
                snake2.dx = 0
                snake2.dy = -snake2.speed #SPEED
                snake2.direction = 'up'
            elif event.key == pygame.K_a and snake2.direction != 'right':
                snake2.dx = -snake2.speed #SPEED
                snake2.dy = 0
                snake2.direction = 'left'
            elif event.key == pygame.K_d and snake2.direction != 'left':
                snake2.dx = snake2.speed #SPEED
                snake2.dy = 0
                snake2.direction = 'right'
            '''elif event.key == pygame.K_1:
                snake1.is_growing = True
            elif event.key == pygame.K_2:
                snake2.is_growing = True'''


    '''if snake1.blocks[0][0] < 0:
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
        snake2.blocks[0][1] = 0'''

    if snake1.blocks[0][0] < 15 or snake1.blocks[0][0] > GAMEZONE_WIDTH:
        THE_END = True
    if snake2.blocks[0][0] < 15 or snake2.blocks[0][0] > GAMEZONE_WIDTH:
        THE_END = True
    if snake1.blocks[0][1] < 15 or snake1.blocks[0][1] > GAMEZONE_HEIGHT:
        THE_END = True
    if snake2.blocks[0][1] < 15 or snake2.blocks[0][1] > GAMEZONE_HEIGHT:
        THE_END = True



    if snake1.blocks[0] in snake2.blocks[:] or snake2.blocks[0] in snake1.blocks[:]:
        #game_over()
        THE_END = True
    
    if snake1.eat(apple):
        snake1.score += 10
        if snake1.score % 3 == 0:
            snake1.speed += 2
        snake1.is_growing = True
        apple.create()

    if snake2.eat(apple):
        snake2.score += 10
        if snake2.score % 3 == 0:
            snake2.speed += 2
        snake2.is_growing = True
        apple.create()

    screen.fill(LIGHT_BROWN)
    screen.blit(gamezone, [30, 30])
    screen.blit(blue_score, [35, 5])
    screen.blit(red_score, [850, 5])
    pygame.display.flip()

    snake1_score = font_small.render(str(snake1.score), True, BLACK)
    snake2_score = font_small.render(str(snake2.score), True, BLACK)
    screen.blit(snake1_score, (190, 5))
    screen.blit(snake2_score, (990, 5))

    snake1.move()
    gamezone.fill(BLACK)
    #snake2.move()
    #gamezone.fill(BLACK)
    snake1.draw(BLUE)
    #snake2.draw(RED)
    apple.draw()
    pygame.display.flip()
