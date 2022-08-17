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
        self.compare()

    def welcome(self):
        pass

    def rules(self):
        pass

    def compare(self):
        gesture1 = self.human_player.select_gesture()
        ai_gesture = self.ai_player.select_gesture()
        if gesture1 == ai_gesture:
            print("It's a tie")
        elif gesture1 == "Rock":
            if ai_gesture == "Scissors":
                print("Rock smashes scissors! You win!")
            elif ai_gesture == "Lizard":
                print("Rock crushes lizard! You win!")
            elif ai_gesture == "Spock":
                print("Spock vaporizes rock! You lose.")
            else: 
                print("Paper covers rock! You lose.")
        elif gesture1 == "Paper":
            if
        elif gesture1 == "Scissors":
            if
        elif gesture1 == "Lizard":
            if
        elif gesture1 == "Spock":
            if
        # elif self.ai_player.select_gesture == "Rock":
        #     if AI ai_gesture == "scissors":
        #         print("win")
        #     else:
        #         print("you lose")
        pass

    def game_mode(self):
        pass

    def display_winner(self):
        pass

    def play_again(self):
        pass