import pygame
import classSnake
import snake

colors = {
        "red":(255,0,0),
        "green":(0,255,0),
        "blue":(0,0,255)
        }

def genSquare(block_color):
    # generate black square
    sqr = pygame.Surface(snake.block_dim)
    sqr.fill(snake.bg_color)
    # generate smaller colored square
    border_size = 2
    col_sqr = pygame.Surface((
        snake.block_dim[0] - border_size,
        snake.block_dim[1] - border_size
        ))
    col_sqr.fill(colors[block_color])
    # put colored square on black square
    sqr.blit(col_sqr, (border_size, border_size))
    return sqr

def blitBlock(block, screen):
    sqr = genSquare(block.color)
    screen.blit(sqr, worldToReal(block.position))

def drawWorld(world, screen):
    rows, cols = snake.gamesize
    for key, layer in world.layers.iteritems():
        for r in range(rows):
            for c in range(cols):
                if (layer[r][c] != 0):
                    space = layer[r][c]
                    blitBlock(space, screen)

def worldToReal(pos):
    x = snake.screensize[0] / snake.gamesize[0]
    y = snake.screensize[1] / snake.gamesize[1]

    return (pos[0] * x, pos[1] * y)
