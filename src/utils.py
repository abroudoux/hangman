import os

class Utils:
    def __init__(self):
        self.__path = None
        self.__words_list_path = None

    def get_words_file(self):
        __path = os.path.abspath(os.path.dirname(__file__))
        __words_list_path = "../ressources/data/words.txt"
        words_file = os.path.join(__path, __words_list_path)

        return words_file

    def get_file(self, file_name):
        self.__path = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(self.__path, file_name)

        return file