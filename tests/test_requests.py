import unittest

from lib.requests import Request

class TestRequest(unittest.TestCase):
    def setUp(self):
        self.request = Request()

    def test_Request_init(self):
        request = Request()
        self.assertEqual(request.user_input, "")

        request = Request("move north")
        self.assertEqual(request.user_input, "move north")

        request = Request(user_input="move south")
        self.assertEqual(request.user_input, "move south")
