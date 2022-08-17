from operator import ge
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
            return gesture
        elif gesture == "Paper":
            return gesture
        elif gesture == "Scissors":
            return gesture
        elif gesture == "Lizard":
            return gesture
        elif gesture == "Spock":
            return gesture


ai_player = Player("Siri")