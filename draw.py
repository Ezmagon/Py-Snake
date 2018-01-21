import pygame
import classSnake
import snake

colors = {
        "red":(255,0,0),
        "green":(0,255,0),
        "blue":(0,0,255)
        }

def genSquare(block_color, block_dim):
    sqr = pygame.Surface(block_dim)
    sqr.fill(colors[block_color])
    return sqr

def drawBlock(block, screen):
    sqr = genSquare(block.color)
    screen.blit(sqr, block.position)
