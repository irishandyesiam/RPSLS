from player import Player

class Human(Player):
    def __init__(self) -> None:
        super().__init__("Chester")

    def select_gesture(self):
        gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        gesture = input(f"Please select a gesture {gestures}")
        print(f"You have selected {gesture}")
        if gesture == "Rock":
            return gesture
        elif gesture == "Paper":
            return gesture
        elif gesture == "Scissors":
            return gesture
        elif gesture == "Lizard":
            return gesture
        elif gesture == "Spock":
            return gesture
        else: 
            print("Try again")
            self.select_gesture()


human_player = Player("Chester")