from HvsAI import AI 
from HvsH import Human

class Game:

    def __init__(self) -> None:
        self.human_player = Human()
        self.human_player2 = Human() or AI()

    def run_game(self):
        self.welcome()
        self.rules()
        self.game_mode()
        self.play_again()

    def welcome(self):
        print("Welcome to RPSLS. Let's GGGGOOOOOO!!!!")
        print("")

    def rules(self):
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")

    def display_winner(self):
        if self.human_player.score >= 2:
            print("Congrats! Player 1 wins!")
        elif self.human_player2.score >= 2:
            print("Congrats! Player 2 wins!")
        self.play_again()
    
    def game_mode(self):
        game_select = input(f"Which game mode do you want to play? single player or multi player")
        if game_select == "single player":
            self.human_player2 = AI()
            self.game_play()
        elif game_select == "multi player":
            self.game_play()
        else:
            print("Please type better.")
            self.game_mode()    
   
    def game_play(self):
        gesture1 = self.human_player.select_gesture()
        ai_gesture = self.human_player2.select_gesture()
        
        if gesture1 == ai_gesture:
            print("It's a tie")
        elif gesture1 == "Rock":
            if ai_gesture == "Scissors":
                print("Rock crushes scissors! Player 1 wins!")
                self.human_player.tally_score()
            elif ai_gesture == "Lizard":
                print("Rock crushes lizard! Player 1 wins!")
                self.human_player.tally_score()
            elif ai_gesture == "Spock":
                print("Spock vaporizes rock! Player 2 wins!")
                self.human_player2.tally_score()
            else: 
                print("Paper covers rock! Player 2 wins!")
                self.human_player2.tally_score()
        elif gesture1 == "Paper":
            if ai_gesture == "Rock":
                print("Paper covers rock! Player 1 wins!")
                self.human_player.tally_score()
            elif ai_gesture == "Scissors":
                print("Scissors cuts paper! Player 2 wins!")
                self.human_player2.tally_score()
            elif ai_gesture == "Lizard":
                print("Lizard eats paper! Player 2 wins!")
                self.human_player2.tally_score()
            else:
                print("Paper disproves Spock! Player 1 wins!")
                self.human_player.tally_score()
        elif gesture1 == "Scissors":
            if ai_gesture == "Rock":
                print("Rock crushes scissors! Player 2 wins!")
                self.human_player2.tally_score()
            elif ai_gesture == "Paper":
                print("Scissors cuts paper! Player 1 wins!")
                self.human_player.tally_score()
            elif ai_gesture == "Lizard":
                print("Scissors decapitates lizard! Player 1 wins!")
                self.human_player.tally_score()
            else:
                print("Spock smashes scissors! Player 2 wins!")
                self.human_player2.tally_score()
        elif gesture1 == "Lizard":
            if ai_gesture == "Spock":
                print("Lizard poisons Spock! Player 1 wins!")
                self.human_player.tally_score()
            elif ai_gesture == "Paper":
                print("Lizard eats Paper! Player 1 wins!")
                self.human_player.tally_score()
            elif ai_gesture == "Rock":
                print("Rock crushes Lizard! Player 2 wins!")
                self.human_player2.tally_score()
            else:
                print("Scissors decapitates Lizard! Player 2 wins!")
                self.human_player2.tally_score()
        elif gesture1 == "Spock":
            if ai_gesture == "Scissors":
                print("Spock smashes Scissors! Player 1 wins!")
                self.human_player.tally_score()
            elif ai_gesture == "Rock":
                print("Spock vaporizes Rock! Player 1 wins!")
                self.human_player.tally_score()
            elif ai_gesture == "Lizard":
                print("Lizard poisons Spock! Player 2 wins!")
                self.human_player2.tally_score()
            else:
                print("Paper disproves Spock! Player 2 wins!")
                self.human_player2.tally_score()
       
        print(f"Player 1 score at {self.human_player.score}.")
        print(f"Player 2 score at {self.human_player2.score}.")
        if self.human_player.score == 2:
            self.display_winner()
        elif self.human_player2.score == 2:
            self.display_winner()
        self.game_play()  
       
    def play_again(self):
        decide = input("Would you like to play again? Y/N")
        if decide == "Y":
            self.game_mode()
        elif decide == "N":
            print("Goodbye")
            exit(0)
        

        


    
