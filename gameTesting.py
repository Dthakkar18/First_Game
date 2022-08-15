import pygame

from pygame.locals import *

#define a object by a class
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()

        #define demension of surface/square
        self.surf = pygame.Surface((25, 25))

        #define color of surface
