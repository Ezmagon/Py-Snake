#!/usr/bin/python2

import pygame, math
import classSnake, draw, world, fruit

screensize = (400,400)
gamesize = (20, 20)
block_dim = (math.floor(screensize[0]/gamesize[0]),math.floor(screensize[1]/gamesize[1]))
bg_color = (0,0,0)

# main function
    
def main ():
    screen = pygame.display.set_mode(screensize)
    snake = classSnake.Snake()
    clock = pygame.time.Clock()
    snakeworld = world.World(gamesize)
    count = 1
    newFruit = ''
    # main loop
    while(True):
        # for every tick in clock
        clock.tick(2)
        # check for events
        event = pollEvents()
        if event:
            snake.direction = event
            event = ''
        # clear screen
        screen.fill(bg_color)
        # move snake
        if count == 1:
           newFruit = fruit.generateFruit(snakeworld)
           count = count + 1
        hasGrown = snake.move(snakeworld)
        if hasGrown:
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
        direction = keypresses[keystroke[0].__dict__["key"]]
        if direction == "quit":
            pygame.display.quit()
            exit()
        return direction
    pygame.event.clear()

keypresses = {
        276:"left",
        273:"up",
        275:"right",
        274:"down",
        27:"quit"
        }

if (__name__ == "__main__"):
    main()
    exit()
