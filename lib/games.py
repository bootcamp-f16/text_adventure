from lib.rooms import rooms_builder
from lib.requests import Request
from lib.responses import Response
from lib.actions import Action
from lib.io_utils import clear_screen, draw, prompt

import lib.game_actions as game_actions

class Game():
    def __init__(self):
        super().__init__()
        self.current_room = None
        self.actions = [
            Action('echo', take_action=game_actions.echo_action)
        ]

    def setup_game(self, rooms_builder=rooms_builder):
        self.current_room = rooms_builder()


    def run(self,
        clear_screen=clear_screen,
        draw=draw,
        prompt=prompt):

        response = Response()

        while True:
            clear_screen()
            draw(self.current_room.draw())
            draw("="*60)
            draw(response.draw())
            user_input = prompt()
            request = Request(user_input)
            response = Response()

            for action in self.actions:
                if(action.should_take_action(request)):
                    action.take_action(request, response, self)

            # Clear Screen
            # Draw current room (print the text need for room)
            # Draw response from previous user input
            # Request user input
            # Process user input
            # Test for exit cases (win, lose, user exits)

