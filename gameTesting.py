import pygame

from pygame.locals import *

#define a object by a class
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()

        #define demension of surface/square
        self.surf = pygame.Surface((25, 25))

        #define color of surface
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()

# initialize game
pygame.init()

# deminsions of screen
screen = pygame.display.set_mode((800, 600))

# create square objs
square1 = Square()

# game loop var
gameOn = True

# game loop
while gameOn:
    #loop through the event queue
    for event in pygame.event.get():

        # check for a key press down
        if event.type == KEYDOWN:

            # if backspace key pressed
            if event.key == K_BACKSPACE:
                gameOn = False

            # if right arrow clicked
            if event.key == K_RIGHT:
                print("moving right!")
                x += 5


        # check for QUIT event
        elif event.type == QUIT:
            gameOn = False

    # where square will be displayed
    x = 40
    y = 40
    screen.blit(square1.surf, (x, y))

    # update display 
    pygame.display.flip()
