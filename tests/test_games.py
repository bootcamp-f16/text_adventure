import unittest

from lib.games import Game

class Request():

    def get(self, url):
        return self
    def json(self):
        return [
            {
                "name": "test 1",
            },
            {
                "name": "test 2",
            },
        ]

class TestGames(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    def test_Game_init(self):
        self.assertEqual(self.game.current_room, None)

    def test_Game_setup_sets_current_room(self):
        def rooms_builder():
            return "room builder"

        self.game.setup_game(rooms_builder=rooms_builder, requests=Request())
        self.assertEqual(self.game.current_room, rooms_builder())
