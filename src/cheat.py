from src.utils import Utils

class Cheat:
    def __init__(self):
        self.utils = Utils()

        self.list_words = self.utils.get_words_file()