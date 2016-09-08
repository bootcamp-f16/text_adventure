def echo_action(request, response, game):
    request.action_taken = True
    response.addOutput(request.user_input)

def exit_action(request, response, game):
    request.action_taken = True
    response.addOutput("THANKS FOR PLAYING!!")
    game.set_exit()

def help_action(request, response, game):
    """
    Iterate through available actions to create a help list for the user
    TODO: This is not DRY (we are repeating the run loop), should clean this up
    """

    actions = []
    for action in game.actions:
        actions.append(action.verb)

    for action in game.current_room.actions:
        actions.append(action.verb)

    if game.current_room.npc is not None:
        for action in game.current_room.npc.actions:
            actions.append(action.verb)

    if game.current_room.clue is not None:
        for action in game.current_room.clue.actions:
            actions.append(action.verb)

    request.action_taken = True
    response.addOutput("Possible Actions:")
    response.addOutput("\n".join(sorted(actions)))