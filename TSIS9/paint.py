import pygame, random

# (x1, y1), (x2, y2)
# A = y2 - y1
# B = x1 - x2
# C = x2 * y1 - x1 * y2
# Ax + By + C = 0
# (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)

BLACK = [0, 0, 0]
GRAY = [192, 192, 192]
BROWN = [153, 76, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
ORANGE = [255, 127, 0]
YELLOW = [255, 255, 0]
GREEN = [0, 255, 0]
LIGHTBLUE = [0, 255, 255]
BLUE = [0, 0, 255]
PURPLE = [255, 0, 255]
PINK = [255, 0, 127]

class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline = None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
            
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('Calibri', 20)
            text = font.render(self.text, True, BLACK)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True 
        return False



def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)

def main():
    screen = pygame.display.set_mode((800, 700))
    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, [0, 100], [800, 100], 2)

    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10

    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }

    black_button = Button(BLACK, 100, 5, 80, 40)
    brown_button = Button(BROWN, 100, 50, 80, 40)
    gray_button = Button(GRAY, 200, 5, 80, 40)
    red_button = Button(RED, 200, 50, 80, 40)
    orange_button = Button(ORANGE, 300, 5, 80, 40)
    yellow_button = Button(YELLOW, 300, 50, 80, 40)
    green_button = Button(GREEN, 400, 5, 80, 40)
    lightblue_button = Button(LIGHTBLUE, 400, 50, 80, 40)
    blue_button = Button(BLUE, 500, 5, 80, 40)
    purple_button = Button(PURPLE, 500, 50, 80, 40)
    pink_button = Button(PINK, 600, 5, 80, 40)
    eraser_button = Button(WHITE, 600, 50, 80, 40)

    black_button.draw(screen, BLACK)
    gray_button.draw(screen, BLACK)
    brown_button.draw(screen, BLACK)
    red_button.draw(screen, BLACK)
    orange_button.draw(screen, BLACK)
    yellow_button.draw(screen, BLACK)
    green_button.draw(screen, BLACK)
    lightblue_button.draw(screen, BLACK)
    blue_button.draw(screen, BLACK)
    purple_button.draw(screen, BLACK)
    pink_button.draw(screen, BLACK)
    eraser_button.draw(screen, BLACK)

    while True:

        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_UP:
                    radius += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                pygame.draw.circle(screen, color, event.pos, radius)
                draw_on = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    drawLine(screen, last_pos, event.pos, radius, color)
                    # pygame.draw.circle(screen, color, event.pos, radius)
                last_pos = event.pos
        pygame.display.flip()

    pygame.quit()

main()