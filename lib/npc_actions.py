
def overlord_talk_action(request, response, game):
    request.action_taken = True

    response.addOutput("""
OVERLORD Responds: MOVE SOUTH and INVESTIGATE each room.
Come back here and ANSWER my question. Do so before you starve to death.
I want you to tell me which repo I am thinking about that belongs to the
bootcamp-f16 organization.
""")
