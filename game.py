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

    def display_winner(self):
        if self.human_player.score >= 2:
            print("Congrats! Human wins!")
        elif self.ai_player.score >= 2:
            print("AI wins! Bye bye human race.")
        self.play_again()
       

    def compare(self):
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
       
        print(f"Human score at {self.human_player.score}.")
        print(f"AI score at {self.ai_player.score}.")
        if self.human_player.score == 2:
            self.display_winner()
        elif self.ai_player.score == 2:
            self.display_winner()
        self.compare()
        
        
        
       
        

        
    def game_mode(self):
        pass

    

    def play_again(self):
        pass