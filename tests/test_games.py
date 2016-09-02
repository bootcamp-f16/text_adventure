import unittest

from lib.games import Game

class TestGames(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    def test_Game_init(self):
        self.assertEqual(self.game.current_room, None)

    def test_Game_setup_sets_current_room(self):
        def rooms_builder():
            return "room builder"

        self.game.setup_game(rooms_builder=rooms_builder)
        self.assertEqual(self.game.current_room, rooms_builder())
