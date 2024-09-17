import os

class Art:
    def __init__(self):
        self.art = ""
        self.title = ""

        self.path = os.path.abspath(os.path.dirname(__file__))
        self.hangman_path = "../ressources/hangman"
        self.hangman_title = "../ressources/title"
        self.hangman_art = os.path.join(self.path, self.hangman_path)
        self.hangman_title = os.path.join(self.path, self.hangman_title)

        self.__start()

    def __start(self):
        self.title = self.__read_ascii_art(self.hangman_title)
        print(self.title)

    def __read_ascii_art(self, file):
        art = open(file).read()

        return art
