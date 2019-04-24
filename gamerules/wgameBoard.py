class Board():
    def __init__(self, n):
        self.n = n
        self.pieces = [None]*self.n
        for i in range(self.n):
            self.pieces[i] = [0]*self.n

    def __getitem__(self, index):
        return self.pieces[index]

    def get_empty_positions(self, playerNum):
        moves = set()
        for y in range(self.n):
            for x in range(self.n):
                if self[x][y] == 0:
                    moves.add((x, y))
        return list(moves)

    def has_empty_positions(self):
        for y in range(self.n):
            for x in range(self.n):
                if self[x][y] == 0:
                    return True
        return False

    def execute_move(self, move, playerNum):
        (x,y) = move
        assert self[x][y] == 0
        self[x][y] = playerNum