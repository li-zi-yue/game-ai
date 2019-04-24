from Coach import Coach
from gamerules.wgame import wgame as Game
from ai.tensorflow.NNet import NNetWrapper as nn
from utils import *
# from Coach import Coach
# from othello.OthelloGame import OthelloGame as Game
# from othello.tensorflow.NNet import NNetWrapper as nn
# from utils import *

args = dotdict({
    'numIters': 20,
    'numEps': 100,
    'tempThreshold': 15,
    'updateThreshold': 0.55,
    'maxlenOfQueue': 200000,
    'numMCTSSims': 25,
    'ExecutePlayCompare': 40,
    'cpuct': 1,

    'checkpoint': './temp/0417',
    'load_model': False,
    'load_folder_file': ('/dev/models/8x100x50','best.pth.tar'),
    'numItersForTrainExamplesHistory': 20,

})


if __name__=="__main__":
    g = Game(6)
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    if args.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()
