from re import S
import pygame

from pygame.locals import *

# initialize game
pygame.init()

# deminsions of screen
screen = pygame.display.set_mode((800, 600))

# create player class
class Player(object):
    def __init__(self, xcord, ycord, width, height, color, step):
        self.x = xcord
        self.y = ycord
        self.width = width
        self.height = height
        self.step = step
        self.color = color
        
    def draw(self, screen):
        # draw obj on screen
        pygame.draw.rect(screen, (self.color), (self.x, self.y, self.width, self.height))
        
    def moveRight(self):
        self.x += self.step

    def moveLeft(self):
        self.x -= self.step
    
    def moveUp(self):
        self.y -= self.step
    
    def moveDown(self):
        self.y += self.step

# create obstacle class
class Obstacle(object):
    def __init__(self):
        self.x = 200
        self.y = 100
        self.color = (255, 0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (self.color), (self.x, self.y), 10)

# obj color
color = (0, 200, 255)

# obj starting coordinates
x = 100
y = 100

# obj dimensions
width = 20
height = 20

# obj step (move speed)
step = 4

# create and draw player 
p = Player(x, y, width, height, color, step)
p.draw(screen)

# create and draw obstacle
o = Obstacle()
o.draw(screen)

# game loop var
gameOn = True

# game loop
while gameOn:
    pygame.time.delay(10)

    #loop through the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False

    # keys pressed info
    keys = pygame.key.get_pressed()

    # right key press
    if keys[pygame.K_RIGHT]:
        # move obj right
        p.moveRight()
    
    # left key press
    if keys[pygame.K_LEFT]:
        # move obj left
        p.moveLeft()

    # up key press
    if keys[pygame.K_UP]:
        # move obj up
        p.moveUp()
    
    # down key press
    if keys[pygame.K_DOWN]:
        # move obj down
        p.moveDown()

    screen.fill((0, 0, 0))
    p.draw(screen)
    o.draw(screen)
    
    # update display 
    pygame.display.update()

pygame.quit()
