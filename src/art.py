import os

class Art:
    def __init__(self):
        self.hangman = ""
        self.title = ""
        self.win = ""
        self.loose = ""

        self.__path = os.path.abspath(os.path.dirname(__file__))
        self.__ressources_path = "../ressources/"
        self.__hangman_path = self.__ressources_path + "hangman"
        self.__title_path = self.__ressources_path + "title"
        self.__win_path = self.__ressources_path + "win"
        self.__loose_path = self.__ressources_path + "loose"

        self.hangman_file = os.path.join(self.__path, self.__hangman_path)
        self.title_file = os.path.join(self.__path, self.__title_path)
        self.win_file = os.path.join(self.__path, self.__win_path)
        self.loose_file = os.path.join(self.__path, self.__loose_path)

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