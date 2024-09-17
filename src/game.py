from src.ascii import Ascii
from src.utils import Utils
from src.debug import Debug

class Game:
    def __init__(self):
        self.word = ""
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
        self.ascii = Ascii()

        self.words_file = Utils().get_words_file()

        self.__config()

    def __config(self):
        while len(self.word) < 7:
            self.word = Utils().choose_random_word(self.words_file)

        self.len_word = len(self.word)

        for char in self.word:
            self.chars_word.append(char)

        return

    def play(self):
        self.ascii.play()

        debugger = Debug(self)
        debugger.print("The word to guess is:", self.word)

        print("Welcome to the hangman game.")

        while not self.has_loose or not self.has_win:
            self.__check_loose()
            self.__turn()

        return

    def __turn(self):
        self.__print()

        if self.has_win:
            self.__win()
            return

        if self.has_loose:
            self.__loose()
            return

        print(f"Penalities: {self.penalities}.", end=" ") if self.penalities > 0 else None
        print(f"Wrong chars guessed: {self.chars_errors}") if self.chars_errors else None
        print("You can make a guess at any time by typing 'guess'")

        self.__ask_user()

        return

    def __print(self):
        if not self.chars_guesses:
            for char in self.chars_word:
                print(" _ ", end=" ")

            print("")
            return

        __temp_arr = []
        [__temp_arr.insert(i, "") for i in range(len(self.chars_word))]

        for char in self.chars_guesses:
            indexes = [i for i, c in enumerate(self.chars_word) if c == char]
            [__temp_arr.__setitem__(i, char) for i in indexes]

        if self.len_word == len("".join(__temp_arr)):
            self.has_win = True
            return

        formatted_output = ' '.join([char if char != '' else '_' for char in __temp_arr])
        print(formatted_output)
        return

    def __ask_user(self):
        string = str.upper(input("Please enter a letter: "))

        if string == "GUESS":
            guess = str.upper(input("Make a guess: "))

            if not guess == str.upper(self.word):
                print("Wrong guess")
                self.penalities += self.big_penality
                self.guesses += 1
                return

            self.has_win = True
            return

        char = string[0]

        if not char.isalpha():
            print("Please enter a valid character.")
            self.__ask_user()

        if char in self.chars_guesses:
            print("You've already guess this letter. Please chose another one.")
            return

        if char in self.chars_word:
            self.chars_guesses.append(char)
            print("Good guess!")
            return

        if char in self.chars_errors:
            self.penalities += self.little_penality
            return

        self.chars_errors.append(char)
        self.penalities += self.medium_penality

        print("Bad guess")
        return

    def __win(self):
        if self.has_win:
            # self.ascii.win()
            print(f"You've win! Congratulations! The word was {self.word}")
            print(f"You've finished this game with {self.penalities} penalities and {self.guesses}")
            exit(1)

    def __loose(self):
        if self.has_loose:
            # self.ascii.loose()
            print(f"You're such a looser! The word was {self.word}")
            print(f"You've finished this game with {self.penalities} penalities and {self.guesses}")
            exit(1)

    def __check_loose(self):
        if self.penalities >= self.limit_penalities or self.guesses >= self.limit_guesses:
            self.has_loose = True
            return

        return