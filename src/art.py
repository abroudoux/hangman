from src.utils import Utils

class Art:
    def __init__(self):
        self.hangman = ""
        self.title = ""
        self.win = ""
        self.loose = ""

        self.hangman_file = Utils().get_file("../ressources/arts/hangman")
        self.title_file = Utils().get_file("../ressources/arts/title")
        self.win_file = Utils().get_file("../ressources/arts/win")
        self.loose_file = Utils().get_file("../ressources/arts/loose")

    def play(self):
        self.title = self.__read_ascii_art(self.title_file)
        print(self.title)

    def hangman(self):
        self.hangman = self.__read_ascii_art(self.hangman_file)
        print(self.hangman)

    def win(self):
        self.win = self.__read_ascii_art(self.win_file)
        print(self.win)

    def loose(self):
        self.loose = self.__read_ascii_art(self.loose_file)
        print(self.loose)

    def __read_ascii_art(self, file):
        art = open(file).read()

        return art