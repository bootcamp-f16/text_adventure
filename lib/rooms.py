from lib.actions import Action
import lib.room_actions as room_actions
from lib.directions import NORTH, SOUTH, EAST, WEST, room_directions, room_opposite

class Room():
    def __init__(self,
        name="",
        description="",
        monster=None,
        items=None,
        rooms=None):
        
        self.name = name
        self.description = description
        self.monster = monster
        self.items = items or []
        self.rooms = rooms or {}

        self.actions = [
            Action('move', take_action=room_actions.move_action),
        ]

    def draw(self):
        """
        Outputs information for the user to be able to
        visualize the room they are currently in
        """

        room_output = [
            "Room: {}".format(self.name),
            "\nDescription:\n{}".format(self.description),
        ]

        return "\n".join(room_output)

    def add_room(self, direction, room=None):
        new_room = room or Room()
        new_room.rooms[room_opposite[direction]] = self
        self.rooms[direction] = new_room
        return new_room

def rooms_builder():
    """
    Returns a starting room that contains
    a tree of rooms off the starting room
    """

    starting_room = Room(
        name="Starting Point",
        description="This is the first room")

    first_room = Room("Room 1", "Room south of starting room")
    starting_room.add_room(SOUTH, first_room)

    second_room = Room("Room 2", "Room south of the first room")
    first_room.add_room(SOUTH, second_room)

    return starting_room