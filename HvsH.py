from player import Player

class Human(Player):
    def __init__(self) -> None:
        super().__init__("Chester")

    def select_gesture(self):
        gesture = input(f"Please select a gesture {gestures}")

gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

human_player = Player("Chester")