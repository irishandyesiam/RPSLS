from player import Player
from HvsAI import AI 
from HvsH import Human

class Game:

    def __init__(self) -> None:
        self.ai_player = AI()
        self.human_player = Human()
        self.human_player2 = Human()

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
            print("Congrats! Human wins!")
        elif self.ai_player.score >= 2:
            print("AI wins! Bye bye human race.")
        elif self.human_player2 >= 2:
            print("Congrats! Human2 wins!")
        self.play_again()
    
    def game_mode(self):
        game_select = input(f"Which game mode do you want to play? single player or multi player")
        if game_select == "single player":
            self.single_player()
        elif game_select == "multi player":
            self.multi_player()
        else:
            print("Please type better.")
            self.game_mode()    

    def single_player(self):
        gesture1 = self.human_player.select_gesture()
        ai_gesture = self.ai_player.select_gesture()
        
        if gesture1 == ai_gesture:
            print("It's a tie")
        elif gesture1 == "Rock":
            if ai_gesture == "Scissors":
                print("Rock crushes scissors! You win!")
                self.human_player.tally_score()
            elif ai_gesture == "Lizard":
                print("Rock crushes lizard! You win!")
                self.human_player.tally_score()
            elif ai_gesture == "Spock":
                print("Spock vaporizes rock! You lose.")
                self.ai_player.tally_score()
            else: 
                print("Paper covers rock! You lose.")
                self.ai_player.tally_score()
        elif gesture1 == "Paper":
            if ai_gesture == "Rock":
                print("Paper covers rock! You win!")
                self.human_player.tally_score()
            elif ai_gesture == "Scissors":
                print("Scissors cuts paper! You lose!")
                self.ai_player.tally_score()
            elif ai_gesture == "Lizard":
                print("Lizard eats paper! You lose.")
                self.ai_player.tally_score()
            else:
                print("Paper disproves Spock! You win!")
                self.human_player.tally_score()
        elif gesture1 == "Scissors":
            if ai_gesture == "Rock":
                print("Rock crushes scissors! You lose.")
                self.ai_player.tally_score()
            elif ai_gesture == "Paper":
                print("Scissors cuts paper! You win!")
                self.human_player.tally_score()
            elif ai_gesture == "Scissors":
                print("Scissors decapitates lizard! You win!")
                self.human_player.tally_score()
            else:
                print("Spock smashes scissors! You lose.")
                self.ai_player.tally_score()
        elif gesture1 == "Lizard":
            if ai_gesture == "Spock":
                print("Lizard poisons Spock! You win!")
                self.human_player.tally_score()
            elif ai_gesture == "Paper":
                print("Lizard eats Paper! You win!")
                self.human_player.tally_score()
            elif ai_gesture == "Rock":
                print("Rock crushes Lizard! You lose.")
                self.ai_player.tally_score()
            else:
                print("Scissors decapitates Lizard! You lose.")
                self.ai_player.tally_score()
        elif gesture1 == "Spock":
            if ai_gesture == "Scissors":
                print("Spock smashes Scissors! You win!")
                self.human_player.tally_score()
            elif ai_gesture == "Rock":
                print("Spock vaporizes Rock! You win!")
                self.human_player.tally_score()
            elif ai_gesture == "Lizard":
                print("Lizard poisons Spock! You lose.")
                self.ai_player.tally_score()
            else:
                print("Paper disproves Spock! You lose.")
                self.ai_player.tally_score()
       
        print(f"Human score at {self.human_player.score}.")
        print(f"AI score at {self.ai_player.score}.")
        if self.human_player.score == 2:
            self.display_winner()
        elif self.ai_player.score == 2:
            self.display_winner()
        self.single_player()
        
        
    def multi_player(self):
        gesture1 = self.human_player.select_gesture()
        ai_gesture = self.human_player2.select_gesture()
        
        if gesture1 == ai_gesture:
            print("It's a tie")
        elif gesture1 == "Rock":
            if ai_gesture == "Scissors":
                print("Rock crushes scissors! You win!")
                self.human_player.tally_score()
            elif ai_gesture == "Lizard":
                print("Rock crushes lizard! You win!")
                self.human_player.tally_score()
            elif ai_gesture == "Spock":
                print("Spock vaporizes rock! You lose.")
                self.human_player2.tally_score()
            else: 
                print("Paper covers rock! You lose.")
                self.human_player2.tally_score()
        elif gesture1 == "Paper":
            if ai_gesture == "Rock":
                print("Paper covers rock! You win!")
                human_win_counter += 1
                # return human_win_counter
            elif ai_gesture == "Scissors":
                print("Scissors cuts paper! You lose!")
                ai_win_counter += 1
                # return ai_win_counter
            elif ai_gesture == "Lizard":
                print("Lizard eats paper! You lose.")
                ai_win_counter += 1
                # return ai_win_counter
            else:
                print("Paper disproves Spock! You win!")
                human_win_counter += 1
                # return human_win_counter
        elif gesture1 == "Scissors":
            if ai_gesture == "Rock":
                print("Rock crushes scissors! You lose.")
                ai_win_counter += 1
                # return ai_win_counter
            elif ai_gesture == "Paper":
                print("Scissors cuts paper! You win!")
                human_win_counter += 1
                # return human_win_counter
            elif ai_gesture == "Scissors":
                print("Scissors decapitates lizard! You win!")
                human_win_counter += 1
                # return human_win_counter
            else:
                print("Spock smashes scissors! You lose.")
                ai_win_counter += 1
                # return ai_win_counter
        elif gesture1 == "Lizard":
            if ai_gesture == "Spock":
                print("Lizard poisons Spock! You win!")
                human_win_counter += 1
                # return human_win_counter
            elif ai_gesture == "Paper":
                print("Lizard eats Paper! You win!")
                human_win_counter += 1
                # return human_win_counter
            elif ai_gesture == "Rock":
                print("Rock crushes Lizard! You lose.")
                ai_win_counter += 1
                # return ai_win_counter
            else:
                print("Scissors decapitates Lizard! You lose.")
                ai_win_counter += 1
                # return ai_win_counter
        elif gesture1 == "Spock":
            if ai_gesture == "Scissors":
                print("Spock smashes Scissors! You win!")
                human_win_counter += 1
                # return human_win_counter
            elif ai_gesture == "Rock":
                print("Spock vaporizes Rock! You win!")
                human_win_counter += 1
                # return human_win_counter
            elif ai_gesture == "Lizard":
                print("Lizard poisons Spock! You lose.")
                ai_win_counter += 1
                # return ai_win_counter
            else:
                print("Paper disproves Spock! You lose.")
                ai_win_counter += 1
                # return ai_win_counter
       
        print(f"Player 1 score at {self.human_player.score}.")
        print(f"Player 2 score at {self.human_player2.score}.")
        if self.human_player.score == 2:
            self.display_winner()
        elif self.human_player2.score == 2:
            self.display_winner()
        self.multi_player()  
       
    def play_again(self):
        decide = input("Would you like to play again? Y/N")
        if decide == "Y":
            self.game_mode()
        elif decide == "N":
            print("Goodbye")
            exit(0)
        

        


    
