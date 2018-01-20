import draw


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
        self.blocks = initBlocks()
        self.initPositions()
        self.head = self.blocks[0]



    def initBlocks(n=3):
        blocks = []
        if (n > 1):
            for i in range(n):
                blocks.append(block())
        return blocks

    def initPositions(self):
        for block in self.blocks:
            if (self.blocks.index(block) == 0):
                block.setPosition((0,0))
            else:
                #pos = ((self.blocks(self.blocks.index(block) - 1)).position[0] + 16, 0)
                index = self.blocks.index(block)
                prev_pos = self.blocks[index - 1].position
                pos = (prev_pos[0] + 16 , prev_pos[1])

    def move(self, grow=False):
        if (grow == False):
            del self.blocks[-1]
        new_head_pos = addPairs(self.head.position, decodeDirection(self.direction))
        self.blocks.insert(block(), 0)
        self.head.position = new_head_pos

### Some global functions

def addPairs(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])

def decodeDirection(direction):
    directions = {
                left:(-16,0),
                right:(16,0),
                up:(0,16),
                down:(0,-16)}
    return directions[direction]
