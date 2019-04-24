from __future__ import print_function
import sys
from .wgameBoard import Board
import numpy as np

class wgame():
    def __init__(self, n=15, nir=5):
        self.n = n
        self.n_in_row = nir
    
    def getInitBoard(self):
        b = Board(self.n)
        return np.array(b.pieces)
    
    def getBoardSize(self):
        return (self.n, self.n)

    def getActionSize(self):
        return self.n * self.n + 1

    def getNextState(self, board, player, action):
        if action == self.n * self.n:
            return (board, -player)
        b = Board(self.n)
        b.pieces = np.copy(board)
        move = (int(action / self.n), action % self.n)
        b.execute_move(move, player)
        return (b.pieces, -player)

    def getValidMoves(self, board, player):
        valids = [0] * self.getActionSize()
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves = b.get_empty_positions(player)
        if len(legalMoves) == 0:
            valids[-1] = 1
            return np.array(valids)
        for x,y in legalMoves:
            valids[self.n * x + y] = 1
        return np.array(valids)
    
    def getGameEnded(self, board, player):
        b = Board(self.n)
        b.pieces = np.copy(board)
        n = self.n_in_row

        for w in range(self.n):
            for h in range(self.n):
                if (w in range(self.n- n + 1) and board[w][h] != 0 and
                        len(set(board[i][h] for i in range(w, w + n))) == 1):
                    return board[w][h]
                if (h in range(self.n- n + 1) and board[w][h] != 0 and
                        len(set(board[w][j] for j in range(h, h + n))) == 1):
                    return board[w][h]
                if (w in range(self.n- n + 1) and h in range(self.n - n + 1) and board[w][h] != 0 and
                        len(set(board[w + k][h + k] for k in range(n))) == 1):
                    return board[w][h]
                if (w in range(self.n - n + 1) and h in range(n - 1, self.n) and board[w][h] != 0 and
                        len(set(board[w + l][h - l] for l in range(n))) == 1):
                    return board[w][h]
        if b.has_empty_positions():
            return 0
        return 1e-4
    
    def getState(self, board, player):
        return player * board
        
    def getSymmetries(self, board, pi):
        # mirror, rotational
        assert(len(pi) == self.n**2 + 1)  # 1 for pass
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        l = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l
    
    def stringRepresentation(self, board):
        return board.tostring()

def display(board):
    n = board.shape[0]

    print(" ----------------")
    print("   ", end="")
    for y in range(n):
        print(y, "", end="")
    print("")
    for y in range(n):
        print(y, "|", end="")
        for x in range(n):
            piece = board[y][x]
            if piece == -1:
                print("x ", end="")
            elif piece == 1:
                print("o ", end="")
            else:
                if x ==n:
                    print("-", end="")
                else:
                    print("- ", end="")
        print("|")
    
    print(" ----------------")
