from player import Player
from HvsAI import AI 
from HvsH import Human

class Game:

    def __init__(self) -> None:
        self.ai_player = AI("Siri")
        self.human_player = Human("Chester")

    def run_game(self):
        self.ai_player.select_gesture()
        self.human_player.select_gesture()
        self.human_player.compare()

    def welcome(self):
        pass

    def rules(self):
        pass

    def game_mode(self):
        pass

    def display_winner(self):
        pass

    def play_again(self):
        pass