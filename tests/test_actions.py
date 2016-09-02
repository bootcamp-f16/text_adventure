import unittest

from lib.requests import Request
from lib.responses import Response
from lib.games import Game
from lib.rooms import Room

from lib.actions import Action

class TestActions(unittest.TestCase):
    def setUp(self):
        def rooms_builder():
            return Room()
        self.game = Game()
        self.game.setup_game(rooms_builder=rooms_builder)
        self.response = Response()

    def test_Action_init(self):
        action = Action('say')
        self.assertEqual(action.verb, 'say')
        self.assertEqual(action.content, '')

        action = Action('say', 'hi')
        self.assertEqual(action.verb, 'say')
        self.assertEqual(action.content, 'hi')

    def test_Action_should_take_action(self):
        action = Action("say")
        request = Request("say hi")

        result = action.should_take_action(request)
        self.assertTrue(result)

        action = Action("say")
        request = Request("move north")

        result = action.should_take_action(request)
        self.assertFalse(result)

