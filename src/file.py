import os
import random

class FileUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_file(file_path):
        path = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(path, file_path)
        return file

    @staticmethod
    def read_file(file_name):
        content = open(file_name).read().splitlines()
        return content

    @staticmethod
    def clean_file(file_name):
        open(file_name, 'w').close()
        return

    @staticmethod
    def write_file(file_name, new_content):
        with open(file_name, 'a') as f:
            f.write('\n'.join(new_content))
        return

    def replace_best_score(self, file_name, new_best_score):
        self.clean_file(file_name)
        self.write_file(file_name, new_best_score)

    def get_words_file(self):
        words_file_path = "../ressources/data/words.txt"
        words_file = self.get_files(words_file_path)
        return words_file

    def choose_random_word_in_file(self, file_name):
        lines = self.read_file(file_name)
        chosen_word = str.upper(random.choice(lines))
        return chosen_word