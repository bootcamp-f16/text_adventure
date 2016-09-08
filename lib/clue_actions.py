from random import choice

def investigate_letters_action(request, response, game):
    request.action_taken = True
    game.player.health -= 5
    letters = [choice(game.repo['name']) for x in range(3)]
    response.addOutput("Three letters of the repo name that I am looking for is {}".format(letters))

def investigate_first_letter_action(request, response, game):
    request.action_taken = True
    game.player.health -= 5
    letter = game.repo['name'][0]
    response.addOutput("The first letter of the repo name that I am looking for is {}".format(letter))