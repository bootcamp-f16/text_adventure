import os

from lib.rooms import rooms_builder


class Game():

    def __init__(self):
        super().__init__()
        self.current_room = None

    def setup_game(self, rooms_builder_func=rooms_builder):
        self.current_room = rooms_builder_func()


    def run(self):
        while True:
            os.system("clear")
            input(">>>")

            # Clear Screen
            # Draw current room (print the text need for room)
            # Draw response from previous user input
            # Request user input
            # Process user input
            # Test for exit cases (win, lose, user exits)