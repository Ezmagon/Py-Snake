class World():
    def __init__(self, size):
        self.__world = []
        row, col = size
        for r in range(row):
            vector = []
            for c in range(col):
                vector.append(0)
            self.__world.append(vector)
    
    def place(self, blocks):
        isList = True
        try:
            len(blocks)
        except:
            isList = False
        if (isList):
            for block in blocks:
                r, c = block.position
                self.__world[r][c] = block

    def show(self):
        for row in self.__world:
            print row
