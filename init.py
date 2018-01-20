import pygame

size = (320,320)
pygame.display.set_mode(size)
# tiled field, 16x16

def genSquare():
    size = (16,16)
    sqr = pygame.Surface(size)
    sqr.fill(255,0,0)
    return sqr


