def echo_action(request, response, game):
    response.addOutput(request.user_input)