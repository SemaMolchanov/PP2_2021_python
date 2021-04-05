import pygame 
import math

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [0, 0, 255]
BLUE = [255, 0, 0]

screen = pygame.display.set_mode([796, 480])
screen.fill([255, 255, 255])
pygame.display.set_caption('function graph')

done = False

cos_points = []
sin_points = []

n = 6
a = 192

for x in range(77, 719):
    y = int(math.cos(x/684 * n * math.pi) * a + 226)
    cos_points.append([x, y])

for x in range(77, 719):
    y = int(math.sin(x/684 * n * math.pi) * a + 226)
    sin_points.append([x, y])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and key.type == pygame.K_ESCAPE:
            done = True

    #frame

    pygame.draw.rect(screen, BLACK, (56, 12, 684, 428), 3)

    #x-axis and y-axis

    pygame.draw.line(screen, BLACK, [56, 226], [740, 226], 3)
    pygame.draw.line(screen, BLACK, [398, 12], [398, 440], 3)

    #left vertical lines

    pygame.draw.line(screen, BLACK, [56, 178], [740, 178], 1)
    pygame.draw.line(screen, BLACK, [56, 130], [740, 130], 1)
    pygame.draw.line(screen, BLACK, [56, 82], [740, 82], 1)
    pygame.draw.line(screen, BLACK, [56, 34], [740, 34], 1)

    #right vertical lines

    pygame.draw.line(screen, BLACK, [56, 274], [740, 274], 1)
    pygame.draw.line(screen, BLACK, [56, 322], [740, 322], 1)
    pygame.draw.line(screen, BLACK, [56, 370], [740, 370], 1)
    pygame.draw.line(screen, BLACK, [56, 418], [740, 418], 1)

    #upper horiszontal lines

    pygame.draw.line(screen, BLACK, [291, 12], [291, 440], 1)
    pygame.draw.line(screen, BLACK, [184, 12], [184, 440], 1)
    pygame.draw.line(screen, BLACK, [77, 12], [77, 440], 1)

    #lower horizontal lines

    pygame.draw.line(screen, BLACK, [505, 12], [505, 440], 1)
    pygame.draw.line(screen, BLACK, [612, 12], [612, 440], 1)
    pygame.draw.line(screen, BLACK, [719, 12], [719, 440], 1)

    #sine and cosine lines

    pygame.draw.lines(screen, BLUE, False, cos_points, 4)
    pygame.draw.lines(screen, RED, False, sin_points, 4)

    pygame.display.flip()

    

