import unittest

from lib.responses import Response

class TestResponse(unittest.TestCase):
    def setUp(self):
        self.response = Response()

    def test_Response_init(self):
        self.assertEqual(self.response.output, [])

    def test_Response_add_output(self):
        response = self.response
        self.assertEqual(response.output, [])
        response.addOutput("Testing 123")
        self.assertEqual(response.output, [
            "Testing 123",
        ])
        
        response.addOutput("Hello world",
            "I can respond more the once")
        self.assertEqual(response.output, [
            "Testing 123",
            "Hello world",
            "I can respond more the once"
        ])
    def test_Response_draw(self):
        output = [
            'Hello',
            'World',
            'this works',
        ]

        self.response.addOutput(*output)
        self.assertEqual(self.response.draw(),
            "\n".join(output))
