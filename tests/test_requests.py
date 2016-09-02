import unittest

from lib.requests import Request

class TestRequest(unittest.TestCase):
    def setUp(self):
        self.request = Request()

    def test_Request_init(self):
        request = Request()
        self.assertEqual(request.user_input, "")
        self.assertIsNotNone(request.input_parse_format)

        request = Request("move north")
        self.assertEqual(request.user_input, "move north")

        request = Request(user_input="move south")
        self.assertEqual(request.user_input, "move south")

    def test_Request_get_verb(self):
        request = Request("")
        self.assertIsNone(request.get_verb())
        request = Request("exit")
        self.assertEqual(request.get_verb(), "exit")
        
        request = Request("move north")
        self.assertEqual(request.get_verb(), "move")

        request = Request("say hello to my little friend")
        self.assertEqual(request.get_verb(), "say")