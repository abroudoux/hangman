from src.game import Game
from src.random import Random

if __name__ == '__main__':
    Random()
    game = Game(random=True).play()
