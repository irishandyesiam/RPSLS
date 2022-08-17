class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    def tally_score(self):
        self.score += 1