from re import S
import pygame

from pygame.locals import *

# initialize game
pygame.init()

# deminsions of screen
screen = pygame.display.set_mode((800, 600))

# create square objs
color = (0, 200, 255)

# obj coordinates
x = 100
y = 100

# obj dimensions
width = 20
height = 20

# obj step
step = 4

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
        x += step
    
    # left key press
    if keys[pygame.K_LEFT]:
        # move obj left
        x -= step

    # up key press
    if keys[pygame.K_UP]:
        # move obj up
        y -= step
    
    # down key press
    if keys[pygame.K_DOWN]:
        # move obj down
        y += step

    # color screen
    screen.fill((0, 0, 0))
    
    # draw obj on screen
    pygame.draw.rect(screen, color, (x, y, width, height))
    
    # update display 
    pygame.display.update()

pygame.quit()
