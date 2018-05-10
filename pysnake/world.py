import snake

class World():
    def __init__(self, size):
        self.size = size
        matrix = self.genmatrix()
        self.layers = {
                "snake":matrix,
                "fruit":matrix
                }
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
                self.layers[block.layer][r][c] = block
        elif (not isList):
            block = blocks
            r, c = block.position
            self.layers[block.layer][r][c] = block

    def show(self):
        for layer in self.layer:
            for row in self.world:
                print row

    def reset(self):
        for key, layer in self.layers.iteritems():
            self.layers[key] = self.genmatrix()

    def genmatrix(self):
        matrix = []
        row, col = self.size
        for r in range(row):
            vector = []
            for c in range(col):
                vector.append(0)
            matrix.append(vector)
        return matrix
