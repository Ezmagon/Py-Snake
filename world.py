import snake

class World():
    def __init__(self, size):
        self.world = []
        self.size = size
        self.reset()
        self.block_pixels = (
                snake.screensize[0] / snake.gamesize[0],
                snake.screensize[1] / snake.gamesize[1]
                )
    
    def place(self, blocks):
        isList = True
        try:
            len(blocks)
        except:
            isList = False
        if (isList):
            for block in blocks:
                r, c = block.position
                self.world[r][c] = block

    def show(self):
        for row in self.__world:
            print row

    def reset(self):
        self.world = []
        row, col = self.size
        for r in range(row):
            vector = []
            for c in range(col):
                vector.append(0)
            self.world.append(vector)

