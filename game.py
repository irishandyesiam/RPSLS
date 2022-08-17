from player import Player
from HvsAI import AI 
from HvsH import Human

class Game:

    def __init__(self) -> None:
        self.ai_player = AI()
        self.human_player = Human()

    def run_game(self):
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
                print("Rock crushes scissors! You win!")
            elif ai_gesture == "Lizard":
                print("Rock crushes lizard! You win!")
            elif ai_gesture == "Spock":
                print("Spock vaporizes rock! You lose.")
            else: 
                print("Paper covers rock! You lose.")
        elif gesture1 == "Paper":
            if ai_gesture == "Rock":
                print("Paper covers rock! You win!")
            elif ai_gesture == "Scissors":
                print("Scissors cuts paper! You lose!")
            elif ai_gesture == "Lizard":
                print("Lizard eats paper! You lose.")
            else:
                print("Paper disproves Spock! You win!")
        elif gesture1 == "Scissors":
            if ai_gesture == "Rock":
                print("Rock crushes scissors! You lose.")
            elif ai_gesture == "Paper":
                print("Scissors cuts paper! You win!")
            elif ai_gesture == "Scissors":
                print("Scissors decapitates lizard! You win!")
            else:
                print("Spock smashes scissors! You lose.")
        elif gesture1 == "Lizard":
            if ai_gesture == "Spock":
                print("Lizard poisons Spock! You win!")
            elif ai_gesture == "Paper":
                print("Lizard eats Paper! You win!")
            elif ai_gesture == "Rock":
                print("Rock crushes Lizard! You lose.")
            else:
                print("Scissors decapitates Lizard! You lose.")
        elif gesture1 == "Spock":
            if ai_gesture == "Scissors":
                print("Spock smashes Scissors! You win!")
            elif ai_gesture == "Rock":
                print("Spock vaporizes Rock! You win!")
            elif ai_gesture == "Lizard":
                print("Lizard poisons Spock! You lose.")
            else:
                print("Paper disproves Spock! You lose.")
    
    def game_mode(self):
        pass

    def display_winner(self):
        pass

    def play_again(self):
        pass