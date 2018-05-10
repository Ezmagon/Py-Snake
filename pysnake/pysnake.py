#!/usr/bin/env/ python2

import pygame, math
from pysnake import *

# define some globals
screensize = (700,700)
gamesize = (20, 20)

# calculate the block dimensions in pixels
block_dim = (math.floor(screensize[0]/gamesize[0]),math.floor(screensize[1]/gamesize[1]))

# define background color
bg_color = (0,0,0)

# main function
    
def main ():
    screen = pygame.display.set_mode(screensize)
    while(True):
        snake = classSnake.Snake()
        clock = pygame.time.Clock()
        snakeworld = world.World(gamesize)
        count = 1
        newFruit = ''
        isGameOver = False
        # main loop
        while(isGameOver == False):
            # for every tick in clock
            clock.tick(4)
            # check for events
            event = pollEvents()
            if event:
                if event == "break":
                    isGameOver = True
                else:
                    snake.setDirection(event)
                    event = ''
            # clear screen
            screen.fill(bg_color)
            # move snake
            if count == 1:
               newFruit = fruit.generateFruit(snakeworld)
               count = count + 1
            hasGrown = snake.move(snakeworld)
            if hasGrown == 2:
                isGameOver = True
            elif hasGrown == 1:
                newFruit = fruit.generateFruit(snakeworld)
    
            # reset world
            snakeworld.reset()
            #place snake into world  
            snakeworld.place(snake.blocks)
            # place fruit into world if there is no fruit
            snakeworld.place(newFruit)
            # draw world
            draw.drawWorld(snakeworld, screen)
            # update screen
            pygame.display.flip()
            # if collision with wall
            #    pbc
            #check collission food/snake
            #    if food is eaten
            #        place food again
            #    if collision
            #        game over
            #        break from loop
            #run main

def pollEvents():
    keystroke = pygame.event.get([2,3])
    if keystroke:
        if keystroke[0].__dict__["key"] in keypresses:
            direction = keypresses[keystroke[0].__dict__["key"]]
            if direction == "quit":
                pygame.display.quit()
                exit()
            if direction == "restart":
                return "break"
            return direction
    pygame.event.clear()

keypresses = {
        276:"left",
        273:"up",
        275:"right",
        274:"down",
        27:"quit",
        13:"restart"
        }

if (__name__ == "__main__"):
    main()
    exit()
