import random
import os

from src.art import Art

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
        self.limit_guesses = 3
        self.has_win = False

        self.__path = os.path.abspath(os.path.dirname(__file__))
        self.__words_list_path = "../ressources/words.txt"
        self.words_file = os.path.join(self.__path, self.__words_list_path)

        self.__config(self.words_file)
        self.__play()

    def __play(self):
        Art().play()

        print("Welcome to the hangman game.")
        print("The word to guess is:", self.word, self.chars_word)

        self.__turn()

    def __config(self, file):
        while len(self.word) < 7:
            lines = open(file).read().splitlines()
            self.word = str.upper(random.choice(lines))

        self.len_word = len(self.word)

        for char in self.word:
            self.chars_word.append(char)

        return

    def __turn(self):
        self.__print()

        if self.has_win:
            Art().win()
            print("You've won!")
            return

        if self.penalities >= self.limit_penalities:
            Art().loose()
            print("You've lost!")
            return

        while self.penalities < self.limit_penalities or not self.has_win:
            self.__ask_user()
            print(f"Penalities: {self.penalities}. Wrong chars guessed: {self.chars_errors}")
            print("You can make a guess at any time by typing 'guess'")

    def __print(self):
        if not self.chars_guess:
            for char in self.chars_word:
                print(" _ ", end=" ")

            print("")
        else:
            return

    def __ask_user(self):
        string = str.upper(input("Please enter a letter: "))

        if string == "GUESS":
            guess = str.upper(input("Make a guess: "))

            if not guess == str.upper(self.word):
                print("Wrong guess")
                self.penalities += self.big_penality
                return

            self.has_win = True
            return

        char = string[0]

        if not char.isalpha():
            print("Please enter a valid character.")
            self.__ask_user()

        if char in self.chars_word:
            print("Good guess")
            return

        if char in self.chars_errors:
            self.penalities += self.little_penality
            return

        self.chars_errors.append(char)
        self.penalities += self.medium_penality

        print("Bad guess")

        return