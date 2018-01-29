import random
import snake
import classSnake

def generateFruit(snakeworld):
    # try to insert fruit into the world
    newFruit = classSnake.Block(color="green", layer="fruit")
    while(True):
        rand_coord = (random.randint(0, snake.gamesize[0] - 1), random.randint(0, snake.gamesize[1] - 1))
        row, col = rand_coord
        if snakeworld.layers["snake"][row][col] == 0:
            newFruit.position = rand_coord
            break
    return newFruit
