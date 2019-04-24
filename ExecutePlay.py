import numpy as np
import time
from pytorch_classification.utils import Bar, AverageMeter

class ExecutePlay():

    def __init__(self,player1,player2,game,display=None):
        self.player1 = player1
        self.player2 = player2
        self.game = game
        self.display = display

    def playGame(self, details=False):
        players = [self.player2, None, self.player1]
        curPlayer = 1
        board = self.game.getInitBoard()
        it = 0
        while self.game.getGameEnded(board, curPlayer) == 0:
            it += 1
            if details and it == 1:
                assert(self.display)
                print("\n    先手请落子")
                self.display(board)
            m = self.game.getState(board, curPlayer)
            action = players[curPlayer+1](self.game.getState(board, curPlayer))

            valids = self.game.getValidMoves(self.game.getState(board, curPlayer),1)

            if valids[action] == 0:
                print(action)
                assert valids[action] > 0
            board, curPlayer = self.game.getNextState(board, curPlayer, action)
            if details:                 
                assert(self.display)
                print("局数：", str(it), "玩家：", str(-curPlayer))
                self.display(board)
        if details:
            assert(self.display)
            print("游戏结束！局数：",str(it),"结果：",str(self.game.getGameEnded(board, 1)))
            self.display(board)
        return self.game.getGameEnded(board, 1)

    def playManyGames(self, num, details=False):
        eps_time = AverageMeter()
        bar = Bar('比赛进度：', max=num)
        end = time.time()
        eps = 0
        maxeps = int(num)

        num = int(num/2)
        oneWon = 0
        twoWon = 0
        draws = 0
        for _ in range(num):
            gameResult = self.playGame(details=details)
            if gameResult == 1:
                oneWon += 1
            elif gameResult == -1:
                twoWon += 1
            else:
                draws += 1
            bar.suffix = '({eps}/{maxeps}) 本局比赛时间:{et:.3f}s | 总时间:{total:}|预计完成时间:{eta:}\n'.format(eps=eps+1, maxeps=maxeps, et=eps_time.avg, total=bar.elapsed_td, eta=bar.eta_td)
            eps += 1
            eps_time.update(time.time()-end)
            end = time.time()
            

            bar.next()

        self.player1, self.player2 = self.player2, self.player1

        for _ in range(num):
            gameResult = self.playGame(details=details)
            if gameResult == -1:
                oneWon += 1
            elif gameResult == 1:
                twoWon += 1
            else:
                draws += 1
            bar.suffix = '({eps}/{maxeps}) 本局比赛时间:{et:.3f}s | 总时间:{total:}|预计完成时间:{eta:}\n'.format(eps=eps+1, maxeps=maxeps, et=eps_time.avg, total=bar.elapsed_td, eta=bar.eta_td)
            eps += 1
            eps_time.update(time.time() - end)
            end = time.time()
            bar.next()
        bar.finish()

        return oneWon, twoWon, draws
