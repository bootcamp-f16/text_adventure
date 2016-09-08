from parse import parse

class Request():
    def __init__(self, user_input=""):
        self.user_input = user_input
        self.input_parse_format = "{verb:w} {content:>}"
        self.action_taken = False

    def get_verb(self):
        result = parse(self.input_parse_format, self.user_input)

        if result is None:
            result = parse("{verb}", self.user_input)

        return result.named.get('verb') if result else None

    def get_content(self):
        result = parse(self.input_parse_format, self.user_input)

        return result.named.get('content') if result else None