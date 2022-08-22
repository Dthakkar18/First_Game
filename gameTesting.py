from re import S
import pygame
import random

from pygame.locals import *

# initialize game
pygame.init()

# deminsions of screen
screen = pygame.display.set_mode((1000, 800))

# create player class
class Player(object):
    def __init__(self, xcord, ycord, width, height, color, step, screen):
        self.x = xcord
        self.y = ycord
        self.width = width
        self.height = height
        self.step = step
        self.color = color
        self.screen = screen
        
    def draw(self, screen):
        # draw obj on screen
        pygame.draw.rect(screen, (self.color), (self.x, self.y, self.width, self.height))
        
    def moveRight(self):
        if self.x + self.step >= self.screen.get_width():
            self.x = 0
        else:
            self.x += self.step

    def moveLeft(self):
        if self.x - self.step <= 0:
            self.x = self.screen.get_width()
        else:
            self.x -= self.step
    
    def moveUp(self):
        if self.y - self.step <= 0:
            self.y = self.screen.get_height()
        else:
            self.y -= self.step
    
    def moveDown(self):
        if self.y + self.step >= self.screen.get_height():
            self.y = 0
        else:
            self.y += self.step

# create obstacle class
class Obstacle(object):
    def __init__(self):
        self.x = random.randrange(100, 900)
        self.y = random.randrange(100, 700)
        self.color = (255, 0, 0)
        self.step = 1
    
    def draw(self, screen):
        pygame.draw.circle(screen, (self.color), (self.x , self.y), 10)
    
    def move(self, object: Player) -> Player:
        # for the x direction
        if object.x < self.x:
            self.x -= self.step
        else:
            self.x += self.step
        # for the y direction
        if object.y > self.y:
            self.y += self.step
        else:
            self.y -= self.step
        
        



# player color
color = (0, 200, 255)
# player starting coordinates
x = 100
y = 100
# player dimensions
width = 20
height = 20
# player step (move speed)
step = 4
# create and draw player 
player = Player(x, y, width, height, color, step, screen)
player.draw(screen)


# create and draw three obstacles
obstacles = []
for i in range(3):
    obstacle = Obstacle()
    obstacle.draw
    obstacles.append(obstacle)


bullets = []


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

    # trying to implement bullets
    if keys[pygame.K_SPACE]:
        bullet = pygame.Rect(100, 100, 20, 20)
        bullets.append(bullet)
        
    # right key press
    if keys[pygame.K_RIGHT]:
        # move obj right
        player.moveRight()
    
    # left key press
    if keys[pygame.K_LEFT]:
        # move obj left
        player.moveLeft()

    # up key press
    if keys[pygame.K_UP]:
        # move obj up
        player.moveUp()
    
    # down key press
    if keys[pygame.K_DOWN]:
        # move obj down
        player.moveDown()

    screen.fill((0, 0, 0))
    player.draw(screen)

    # move and draw obstacles
    for obstacle in obstacles:
        obstacle.move(player)
        obstacle.draw(screen)
    
    # update display 
    pygame.display.update()

pygame.quit()
