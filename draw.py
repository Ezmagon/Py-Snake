import pygame
import classSnake

colors = {
        "red":(255,0,0),
        "green":(0,255,0),
        "blue":(0,0,255)
        }

def genSquare(block_color):
    sqr = pygame.Surface(block_dim)
    sqr.fill(colors[block_color])
    return sqr

def drawBlock(block):
    screen = pygame.get_surface()
    sqr = genSquare(block.color)
    screen.blit(sqr, block.position)
