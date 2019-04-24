import ExecutePlay
from gamerules.wgame import wgame, display
from gamerules.wgamePlayers import *
from ai.tensorflow.NNet import NNetWrapper as NNet
from MCTS import MCTS
import numpy as np
from utils import *

g = wgame(6)
rp = RandomPlayer(g).play
hp = HumanPlayer(g).play
#gp = GreedyPlayer(g).play

# n = NNet(g)
# n.load_checkpoint('./temp/g/','best.pth.tar')
# args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
# mcts1 = MCTS(g, n, args1)
# np = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))
n1 = NNet(g)
n1.load_checkpoint('./temp/0417/','best.pth.tar')
args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))
print('请选择玩家，输入两个数，中间空格隔开：1.随机玩家 2.神经网络玩家 3.人类玩家')
a = input()
x,y = [int(x) for x in a.split(' ')]

if x == 1:
    p1 = rp
if x == 2:
    p1 = n1p
if x == 3:
    p1 = rp
if y == 1:
    p2 = rp
if y == 2:
    p2 = n1p
if y == 3:
    p2 = rp
e = ExecutePlay.ExecutePlay(p1, p2, g, display=display)

e = ExecutePlay.ExecutePlay(n1p, hp, g, display=display)
print(e.playManyGames(2, details=True))
