#!/usr/bin/python2

import pygame
import classSnake
import draw
import math

block_dim = (math.floor(screensize[0]/10),math.floor(screensize[1]/10))
screensize = (400,400)

# main function
if (__name__ == "__main__"):
    
    def main ():
        screen = pygame.display.set_mode(screensize)
        snake = classSnake.Snake()
        clock = pygame.time.Clock()
       # main loop
        while(True):
       # check for events
       #     for every tick in clock
            clock.tick(1)
       #     move snake
            snake.move()
            # draw snake
            for block in snake.blocks:
                draw.drawBlock(block, screen)  
        #     update screen
            screen.fill(0,0,0)
            screen.flip()
       #         if collision with wall
       #             pbc
       #     check collission food/snake
       #         if food is eaten
       #             place food again
       #         if collision
       #             game over
       #             break from loop
    
    # run main
    main()

    exit()
