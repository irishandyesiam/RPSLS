from player import Player
import random

class AI(Player):
    def __init__(self) -> None:
        super().__init__("Siri")

    def select_gesture(self):
        gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        ai_gesture = random.choice(gestures)
        gesture = ai_gesture
        print(f"Siri selected {gesture}")
        if gesture == "Rock":
            print("Cool")
            return gesture
        # else: 
        #     print("Try again")
        #     self.select_gesture()

ai_player = Player("Siri")