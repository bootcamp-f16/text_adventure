from lib.rooms import rooms_builder
from lib.io_utils import clear_screen, draw, prompt


class Game():

    def __init__(self):
        super().__init__()
        self.current_room = None

    def setup_game(self, rooms_builder=rooms_builder):
        self.current_room = rooms_builder()


    def run(self,
        clear_screen=clear_screen,
        draw=draw,
        prompt=prompt):

        while True:
            clear_screen()
            draw(self.current_room.draw())
            user_input = prompt()

            # Clear Screen
            # Draw current room (print the text need for room)
            # Draw response from previous user input
            # Request user input
            # Process user input
            # Test for exit cases (win, lose, user exits)