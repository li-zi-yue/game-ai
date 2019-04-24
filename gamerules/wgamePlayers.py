import numpy as np

class RandomPlayer():
    def __init__(self, game):
        self.game = game
    
    def play(self, board):
        a = np. random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a]!=1:
            a = np.random.randint(self.game.getActionSize())
        return a

class HumanPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valid = self.game.getValidMoves(board, 1)
        while True:
            a = input()

            x,y = [int(x) for x in a.split(' ')]
            a = self.game.n * x + y if x!= -1 else self.game.n ** 2
            if valid[a]:
                break
            else:
                # print(x, y, a, valid[a], '无效的输入')
                print(x, y, '无效的输入')
                
        return a

class GreedyPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, 1)
        nextone = []
        for a in range(self.game.getActionSize()):
            if valids[a]==0:
                continue
            nextBoard, _ = self.game.getNextState(board, 1, a)
            score = self.game.getScore(nextBoard, 1)
            nextone += [(-score, a)]
        nextone.sort()
        return nextone[0][1]