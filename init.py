import math
import classSnake
import pygame

block_dim = ()
snake = ''

def init(screensize):
    #field is always 10x10
    block_dim = (math.floor(screensize[0]/10),math.floor(screensize[1]/10))
    display.init(screensize)
    pygame.display.set_mode(screensize)
    snake = classSnake.Snake()
