def echo_action(request, response, game):
    request.action_taken = True
    response.addOutput(request.user_input)

def exit_action(request, response, game):
    request.action_taken = True
    response.addOutput("THANKS FOR PLAYING!!")
    game.set_exit()