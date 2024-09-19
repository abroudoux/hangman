from src.file import FileUtils

class Score:
    def __init__(self):
        self.file_utils = FileUtils()

        self.best_score = 0
        self.actual_score = 0
        self.best_score_file_path = "../ressources/data/best_score.txt"
        self.best_score_file = self.file_utils.get_file(self.best_score_file_path)

        self.penalities = 0
        self.guesses = 0
        self.limit_penalities = 30
        self.num_turns = 0

        self.get_best_score()

    def get_best_score(self):
        content = self.file_utils.read_file(self.best_score_file)
        self.best_score = content

        if not content:
            self.best_score = 0
            return
        return

    def compare_scores(self, new_score):
        if new_score < self.best_score:
            return False

        self.best_score = new_score
        return True

    def write_new_best_score(self):
        self.file_utils.write_file(self.best_score_file, self.best_score)
        return

    def increase_score(self, score):
        self.actual_score += score if self.actual_score > 0 else self.actual_score == score
        return

    def decrease_score(self, score):
        self.actual_score -= score if self.actual_score - score > 0 else self.actual_score == score
        return

    def return_score(self):
        return self.actual_score

    def increase_penalities(self, penality):
        self.penalities += penality
        return

    def add_guess(self):
        self.guesses += 1
        return

    def return_scores(self):
        return self.actual_score, self.penalities, self.guesses

    def return_rules(self):
        return self.limit_penalities

    def add_turn(self):
        self.num_turns += 1
        return

    def return_num_turns(self):
        return self.num_turns
