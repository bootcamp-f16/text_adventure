from lib.directions import room_directions

def look_action(request, response, game):
    directions = [direction for direction in game.current_room.rooms.keys()]

    request.action_taken = True
    response.addOutput("There are rooms to the {}".format(", ".join(directions)))

def move_action(request, response, game):
    direction = request.get_content()
    current_room = game.current_room
    new_room = current_room.rooms.get(direction)

    if direction not in room_directions:
        request.action_taken = True
        response.addOutput("{} is an invalid direction".format(direction))
    elif new_room is None:
        request.action_taken = True
        response.addOutput("The is no room to the {}".format(direction))
    else:
        game.current_room = new_room
        game.player.health -= 10
        request.action_taken = True
        response.addOutput("Moved to the room to the {}".format(direction))
