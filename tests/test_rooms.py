import unittest

from lib.directions import NORTH, SOUTH, EAST, WEST, room_directions
from lib.rooms import Room, rooms_builder

class TestRooms(unittest.TestCase):
    def test_Room_init(self):
        room = Room()
        self.assertEqual(room.name, "")
        self.assertEqual(room.description, "")
        self.assertEqual(room.monster, None)
        self.assertEqual(room.items, [])

        room = Room(name="Cuthulu",
            description="This is a room",
            monster={},
            items=[1,2,3])
        self.assertEqual(room.name, "Cuthulu")
        self.assertEqual(room.description, "This is a room")
        self.assertEqual(room.monster, {})
        self.assertEqual(room.items, [1,2,3])

    def test_Room_draw(self):
        room = Room(name="Cuthulu",
            description="This is a room",
            monster={},
            items=[1,2,3])

        result = [
            "Room: {}".format("Cuthulu"),
            "\nDescription:\n{}".format("This is a room"),
        ]
        self.assertEqual(room.draw(), "\n".join(result))
    
    def test_Room_add_room(self):
        starting_room = Room()
        self.assertIsInstance(starting_room.add_room(NORTH), Room)

        south_room = Room(name="South room")

        self.assertIs(starting_room.add_room(SOUTH, south_room), south_room)
        self.assertIs(starting_room.rooms[SOUTH], south_room)

    def test_rooms_builder(self):
        room = rooms_builder()
        self.assertIsInstance(room, Room)



