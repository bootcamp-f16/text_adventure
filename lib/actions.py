
class Action():
    def __init__(self, verb, content=""):
        self.verb = verb
        self.content = content

    def should_take_action(self, request):
        return self.verb == request.get_verb()