import argparse

from src.game import Game


def main():
    parser = argparse.ArgumentParser(description="Options for Game")

    parser.add_argument("--cheat", type=bool, default=False, help="Enable cheat mode")
    parser.add_argument("--random", type=bool, default=False, help="Enable random mode")
    parser.add_argument("--max_len", type=int, default=4, help="Set maximum word length")

    args = parser.parse_args()

    game = Game(cheat=args.cheat, random=args.random, max_len=args.max_len)
    game.play()

if __name__ == '__main__':
    main()
