import random
import os

class Game:
    def __init__(self):
        self.word = ""
        self.len_word = None
        self.chars_word = []
        self.chars_guess = []
        self.chars_errors = []
        self.penalities = 0
        self.little_penality = 3
        self.medium_penality = 5
        self.big_penality = 10
        self.limit_penalities = 30

        self.path = os.path.abspath(os.path.dirname(__file__))
        self.words_list_path = "../ressources/words.txt"
        self.words_list = os.path.join(self.path, self.words_list_path)

        self.__play()

    def __play(self):
        self.word = self.__choose_word(self.words_list)
        self.len_word, self.chars_word = self.__process_word()

        print("Welcome to the hangman game.")
        print("The word to guess is:", self.word, self.chars_word)

        for char in self.chars_word:
            print(" _ ", end = " ")

        print("")

        while self.penalities < self.limit_penalities or len(self.chars_guess) < len(self.chars_word):
            self.__ask_user()
            print(f"Penalities: {self.penalities}. Wrong chars guessed: {self.chars_errors}.")

    def __choose_word(self, file):
        while len(self.word) < 7:
            lines = open(file).read().splitlines()
            self.word = str.upper(random.choice(lines))

        return self.word

    def __process_word(self):
        self.len_word = len(self.word)

        for char in self.word:
            self.chars_word.append(char)

        return self.len_word, self.chars_word

    def __ask_user(self):
        guess = str.upper(input("Please enter a letter: "))

        if guess in self.chars_word:
            print("Good guess")
            return

        if guess in self.chars_errors:
            self.penalities += self.little_penality
            return

        self.chars_errors.append(guess)
        self.penalities += self.medium_penality

        print("Bad guess")

        return