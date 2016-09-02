def echo_action(request, response, game):
    response.addOutput(request.user_input)

def exit_action(request, response, game):
    response.addOutput("THANKS FOR PLAYING!!")
    game.set_exit()