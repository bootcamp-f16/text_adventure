
class Action():
    def __init__(self, verb, content="", take_action=None):
        self.verb = verb
        self.content = content
        self.take_action = take_action

    def should_take_action(self, request):
        return self.verb.lower() == request.get_verb().lower()