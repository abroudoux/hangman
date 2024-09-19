from src.ascii import Ascii
from src.api import WordApi
from src.debug import Debug
from src.cheat import Cheat
from src.file import FileUtils
from src.score import Score

class Game:
    def __init__(self, cheat=False, random=False):
        self.ascii = Ascii()
        self.cheat = Cheat()
        self.debug = Debug(self)
        self.word_api = WordApi()
        self.file_utils = FileUtils()
        self.score = Score()

        self.word = ""
        self.guessed_chars = ""
        self.len_word = None
        self.chars_word = []
        self.chars_guesses = []
        self.chars_errors = []
        self.penalities = 0
        self.little_penality = 3
        self.medium_penality = 5
        self.big_penality = 10
        self.limit_penalities = 30
        self.limit_guesses = 3
        self.guesses = 0
        self.has_win = False
        self.has_loose = False

        self.is_cheat_activated = cheat
        self.is_random_activated = random

        self.__cheat_init()

        if self.is_random_activated:
            self.word = self.word_api.get_word()
        else:
            self.words_file = self.file_utils.get_words_file()
            while len(self.word) < 7:
                self.word = self.file_utils.choose_random_word_in_file(self.words_file)

        self.__get_word_props()

    def __cheat_init(self):
        print("Cheat code activated") if self.is_cheat_activated else None
        return

    def __get_word_props(self):
        self.len_word = len(self.word)

        for char in self.word:
            self.chars_word.append(char)

        return

    def play(self):
        # self.ascii.play()
        self.debug.print_hint("The word to guess is", self.word)

        print("Welcome to the hangman game.")

        while not self.has_loose or self.has_win:
            self.__turn()

        return

    def __turn(self):
        self.__print_hints()
        self.__is_lost()

        if self.has_win:
            self.__has_win()
            return

        if self.has_loose:
            self.__has_loose()
            return

        print(f"Penalities: {self.penalities}.", end=" ") if self.penalities > 0 else None
        print(f"Wrong chars guessed: {self.chars_errors}") if self.chars_errors else None

        if self.is_cheat_activated:
            chars = self.__determine_guessed_chars()
            self.cheat.suggest(chars)

        self.__ask_user()
        return

    def __print_hints(self):
        if not self.chars_guesses:
            for _ in self.chars_word:
                print(" _ ", end=" ")

            print("")
            return

        self.guessed_chars = self.__determine_guessed_chars()
        print(self.guessed_chars)
        return

    def __determine_guessed_chars(self):
        __temp_arr = []
        for i in range(len(self.chars_word)):
            __temp_arr.insert(i, "")

        for char in self.chars_guesses:
            for i, c in enumerate(self.chars_word):
                if c == char:
                    __temp_arr[i] = char

        if self.len_word == len("".join(__temp_arr)):
            self.has_win = True
            return

        guessed_chars = ' '.join([char if char != '' else '_' for char in __temp_arr])
        return guessed_chars

    def __ask_user(self):
        string = str.upper(input("Enter a letter: "))
        self.__ask_user() if not string else None

        if len(string) > 1 and not string == self.word:
            print("Wrong guess")
            self.score.decrease_score(10)
            self.penalities += self.big_penality
            self.guesses += 1
            return
        elif len(string) > 1 and string == self.word:
            self.score.increase_score(15)
            self.has_win = True
            self.__has_win()
            return

        char = string[0]

        if char in self.chars_word:
            self.chars_guesses.append(char)
            self.score.increase_score(5)
            print("Good guess!")
            return

        self.chars_errors.append(char)
        self.score.decrease_score(3)
        self.penalities += self.little_penality

        print("Bad guess")
        return

    def __is_lost(self):
        if self.penalities >= self.limit_penalities or self.guesses >= self.limit_guesses:
            self.has_loose = True
            return
        return

    def __has_win(self):
        if self.has_win:
            # self.ascii.win()
            score = self.score.return_score()
            print(f"You've win! Congratulations! The word was {self.word}")
            print(f"You've finished this game with {self.penalities} penalities and {self.guesses} guesses. Your score is {score}")
            self.__get_best_score()
            exit(1)

    def __has_loose(self):
        if self.has_loose:
            # self.ascii.loose()
            print(f"You're such a looser! The word was {self.word}")
            print(f"You've finished this game with {self.penalities} penalities and {self.guesses} guesses")
            exit(1)

    def __get_best_score(self):
        return