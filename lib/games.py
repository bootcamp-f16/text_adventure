from lib.rooms import rooms_builder
from lib.requests import Request
from lib.responses import Response
from lib.actions import Action
from lib.io_utils import clear_screen, draw, prompt, exit

import lib.game_actions as game_actions

class Game():
    def __init__(self):
        super().__init__()
        self.current_room = None
        self.should_exit = False
        self.actions = [
            Action('echo', take_action=game_actions.echo_action),
            Action('exit', 'game', take_action=game_actions.exit_action),
        ]

    def setup_game(self, rooms_builder=rooms_builder):
        self.current_room = rooms_builder()

    def set_exit(self):
        self.should_exit = True

    def run(self,
        clear_screen=clear_screen,
        draw=draw,
        prompt=prompt,
        exit=exit):

        response = Response()

        while True:
            # Clear Screen
            # Draw current room (print the text need for room)
            # Draw response from previous user input
            # Request user input
            # Process user input
            # Test for exit cases (win, lose, user exits)

            clear_screen()
            draw("GITHUB ADVENTURES")
            draw("="*60)
            draw(self.current_room.draw())
            draw("="*60)
            draw(response.draw())

            # Check if we are exiting before prompting the user
            if self.should_exit:
                return exit()

            user_input = prompt()
            request = Request(user_input)
            response = Response()

            action_taken = False
            for action in self.actions:
                if(action.should_take_action(request)):
                    action_taken = True
                    action.take_action(request, response, self)
            
            if not action_taken:
                response.addOutput("Invalid input")
