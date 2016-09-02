
class Response():
    def __init__(self):
        self.output = []

    def addOutput(self, *args):
        self.output.extend(args)

    def draw(self):
        """
        Renders buffered output to string
        """

        return "\n".join(self.output)