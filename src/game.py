from src.ascii import Ascii
from src.api import WordApi
from src.debug import Debug
from src.cheat import Cheat
from src.file import FileUtils
from src.score import Score

class Game:
    def __init__(self, cheat=False, random=False, max_len=7):
        self.ascii = Ascii()
        self.cheat = Cheat()
        self.debug = Debug(self)
        self.word_api = WordApi()
        self.file_utils = FileUtils()
        self.score = Score()

        self.word = ""
        self.guessed_word = ""
        self.guessed_chars = ""
        self.len_word = None
        self.chars_word = []
        self.guessed_chars_arr = []
        self.chars_errors = []
        self.has_win = False
        self.has_loose = False

        self.is_cheat_activated = cheat
        self.is_random_activated = random
        self.max_len = max_len

        self.__cheat_init()
        self.__api_init()

        if self.is_random_activated:
            self.word = self.word_api.get_word()
        else:
            self.words_file = self.file_utils.get_words_file()
            while len(self.word) < self.max_len:
                self.word = self.file_utils.choose_random_word_in_file(self.words_file)

        self.__get_word_props()

    def __cheat_init(self):
        print("Cheat activated") if self.is_cheat_activated else None
        return

    def __api_init(self):
        print("Word randomly chosen from API") if self.is_random_activated else None
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

        while not self.has_loose or not self.has_win:
            self.__turn()

        return

    def __turn(self):
        score, penalities, guesses, turns = self.score.return_scores()
        limit_penalities = self.score.return_rules()

        self.__check_player_scores(limit_penalities, penalities)
        self.__determine_guessed_chars()

        if self.has_win:
            self.__has_win(score, penalities, guesses, turns)
            return

        if self.has_loose:
            self.__has_loose(penalities, guesses)
            return

        print(f"Score: {score}.", end=" ")
        print(f"Penalities: {penalities}.", end=" ") if penalities > 0 else None
        print(f"Guesses: {guesses}.", end=" ") if guesses > 0 else None
        print(f"Wrong chars guessed: {self.chars_errors}") if self.chars_errors else None

        if self.is_cheat_activated:
            # todo => fix that
            chars = self.__determine_guessed_chars()
            self.cheat.suggest(chars)

        self.__ask_user()
        self.__print_hints()
        self.score.add_turn()
        return

    def __print_hints(self):
        if not self.guessed_chars_arr:
            for _ in self.chars_word:
                print(" _ ", end=" ")

            print("")
            return

        self.guessed_chars = self.__determine_guessed_chars()
        print(self.guessed_chars)
        self.guessed_word = self.guessed_chars.replace(" ", "").replace("_", "")
        return

    def __determine_guessed_chars(self):
        __temp_arr = []

        for i in range(len(self.chars_word)):
            __temp_arr.insert(i, "")

        for char in self.guessed_chars_arr:
            for i, c in enumerate(self.chars_word):
                if c == char:
                    __temp_arr[i] = char

        guessed_chars = ' '.join([char if char != '' else '_' for char in __temp_arr])
        return guessed_chars

    def __ask_user(self):
        string = str.upper(input("Enter a letter: "))
        self.__ask_user() if not string else None

        if len(string) > 1 and not string == self.word:
            print("Wrong guess")
            self.score.decrease_score(10)
            self.score.increase_penalities(10)
            self.score.add_guess()
            return
        elif len(string) > 1 and string == self.word:
            self.score.increase_score(15)
            self.has_win = True
            return

        char = string[0]

        if char in self.chars_word:
            self.guessed_chars_arr.append(char)
            self.score.increase_score(5)
            print("Good guess!")
            return

        self.chars_errors.append(char)
        self.score.decrease_score(3)
        self.score.increase_penalities(3)

        print("Bad guess")
        return

    def __has_win(self, score, penalities, guesses, turns):
        if self.has_win:
            # self.ascii.win()
            print(f"You've win! Congratulations! The word was {self.word}")
            print(f"You've finished this game with {penalities} penalities and {guesses} guesses. Your score is {score}")
            print(f"{turns} turns")
            exit(1)

    def __has_loose(self, penalities, guesses):
        if self.has_loose:
            # self.ascii.loose()
            print(f"You're such a looser! The word was {self.word}")
            print(f"You've finished this game with {penalities} penalities and {guesses} guesses")
            exit(1)

    def __check_player_scores(self, limit_penalities, penalities):
        if penalities >= limit_penalities:
            self.has_loose = True
        elif self.guessed_word == self.word:
            self.has_win = True

        return