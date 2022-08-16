from multiprocessing import RLock
from operator import truediv
from player import Player

class Human(Player):
    def __init__(self) -> None:
        super().__init__("Chester")

    def select_gesture(self):
        gesture = input(f"Please select a gesture {gestures}")
        print(f"You have selected {gesture}")
        if gesture == "Rock":
            print("Cool")
        else: 
            print("Try again")
            self.select_gesture()

gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

human_player = Player("Chester")