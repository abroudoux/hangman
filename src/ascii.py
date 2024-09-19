from src.file import FileUtils

class Ascii:
    def __init__(self):
        self.file_utils = FileUtils()

        self.title = ""
        self.win = ""
        self.loose = ""
        self.cheat = ""

        self.title_file = self.file_utils.get_file("../ressources/ascii/title")
        self.win_file = self.file_utils.get_file("../ressources/ascii/win")
        self.loose_file = self.file_utils.get_file("../ressources/ascii/loose")
        self.cheat_file = self.file_utils.get_file("../ressources/ascii/cheat")

    @staticmethod
    def __read_ascii_art(file):
        art = open(file).read()
        return art

    def play(self):
        self.title = self.__read_ascii_art(self.title_file)
        print(self.title)
        return

    def win(self):
        self.win = self.__read_ascii_art(self.win_file)
        print(self.win)
        return

    def loose(self):
        self.loose = self.__read_ascii_art(self.loose_file)
        print(self.loose)
        return

    def cheat(self):
        self.cheat = self.__read_ascii_art(self.cheat_file)
        print(self.cheat)
        return