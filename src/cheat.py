import re

from src.file import FileUtils

class Cheat:
    def __init__(self):
        self.file_utils = FileUtils()

        self.word = ""
        self.len_word = None
        self.list_words = []
        self.selected_list_word = []

        self.__get_list_words()

    def __get_list_words(self):
        words_file = self.file_utils.get_words_file()
        self.list_words = self.file_utils.read_file(words_file)
        return

    def __filter_with_len(self):
        for word in self.list_words:
            if len(word) == self.len_word:
                self.selected_list_word.append(word)

        return

    def __filter_with_chars_guesses(self):
        pattern = self.word
        print("self.word", self.word)
        regex_pattern = pattern.replace("_", ".")
        regex_pattern = f"^{regex_pattern}$"

        matching_words = [word for word in self.selected_list_word if re.match(regex_pattern, word)]

        print("matching_words", matching_words)
        return

    def __return_word_filtered(self, string):
        self.word = string.replace(" ", "")
        return

    def __return_len_word(self):
        self.len_word = len(self.word)
        return

    def suggest(self, chars):
        self.__return_word_filtered(chars)
        if not self.len_word:
            print("here")
            self.__return_len_word()
            self.__filter_with_len()
        else:
            print("no here")
            self.__filter_with_chars_guesses()

        print("self.selected_list_word", self.selected_list_word)
        return