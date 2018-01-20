#!/usr/bin/python2

import init
import pygame
print "1"
from init import *
print "2"
import draw

# main function
def main ():
    print "beginning"
    screensize = (400,400)
    screen = pygame.display.set_mode(screensize)
    init(screensize)
    clock = pygame.time.Clock()
   # main loop
    while(True):
        print "in loop"
   # check for events
   #     for every tick in clock
        clock.tick(1)
   #     move snake
        snake.move()
        # draw snake
        for block in snake.blocks:
            draw.drawBlock(block)
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
main

exit()
