import draw, snake


########################################
### Class definition for block class ###
########################################
class Block():
    def __init__(self, pos=(0,0)):
        self.position = pos # tuple
        self.color = "red"

########################################
### Class definition for snake class ###
########################################
"""
Methods:
    move(grow=False)
    direction
"""

class Snake():
    def __init__(self, direction="right"):
        self.direction = direction
        self.blocks = self.__initBlocks(3)
        self.__initPositions()
        self.head = self.blocks[0]

    def setDirection(self, direction):
        opposites = (
                ("left","right"),
                ("right","left"),
                ("up","down"),
                ("down","up")
                )
        if ((self.direction,direction) not in opposites):
            self.direction = direction
        else:
            print "opposite direction"

    def __initBlocks(self, n=3):
        blocks = []
        if (n > 1):
            for i in range(n):
                new_block = Block()
                blocks.append(new_block)
        return blocks

    def __initPositions(self):
        for block in self.blocks:
            if (self.blocks.index(block) == 0):
                block.position = (3,0)
            else:
                #pos = ((self.blocks(self.blocks.index(block) - 1)).position[0] + 16, 0)
                index = self.blocks.index(block)
                prev_pos = self.blocks[index - 1].position
                pos = (prev_pos[0] - 1 , prev_pos[1])
                block.position = pos

    def move(self, grow=False):
        ## TODO GROWTH NOT TESTED YET
        if (grow == False):
            del self.blocks[-1]
        new_head_pos = addPairs(self.blocks[0].position, decodeDirection(self.direction))
        new_head_pos = fixWalls(new_head_pos)
        self.blocks.insert(0, Block(pos=new_head_pos))
        self.head = self.blocks[0]

### Some global functions

def addPairs(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])

def decodeDirection(direction):
    directions = {
                "left":(-1,0),
                "right":(1,0),
                "up":(0,-1),
                "down":(0,1)}
    return directions[direction]

def fixWalls(tup):
    x = y = 0
    if (tup[0] < 0):
        x = snake.gamesize[0] - 1
    elif (tup[0] > snake.gamesize[0] - 1):
        x = 0
    else:
        x = tup[0]

    if (tup[1] < 0):
        y = snake.gamesize[1] - 1
    elif (tup[1] > snake.gamesize[1] - 1):
        y = 0
    else:
        y = tup[1]

    return (x,y)
