from src.utils import Utils

class Cheat:
    def __init__(self):
        self.utils = Utils()

        self.len_word = None
        self.list_words = []
        self.selected_list_word = []

    def __get_list_words(self):
        self.list_words = self.utils.get_words_file()
        print(self.list_words)
        return

    def __filter_with_len(self, n):
        self.len_word = n

        for word in self.list_words:
            if len(word) == self.len_word:
                self.selected_list_word.append(word)

        print(self.selected_list_word)
        return