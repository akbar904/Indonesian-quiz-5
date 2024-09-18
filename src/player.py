
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, score):
        if not isinstance(score, int):
            raise TypeError("Score must be a number")
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.score += score

    def reset_score(self):
        self.score = 0
