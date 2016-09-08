from lib.actions import Action
import lib.clue_actions as clue_actions

class Clue():
    def __init__(self):
        super.__init__()
        self.actions = []

class LettersClue(Clue):
    def __init__(self):
        self.actions = [
            Action('investigate', take_action=clue_actions.investigate_letters_action),
        ]

class FirstLetterClue(Clue):
    def __init__(self):
        self.actions = [
            Action('investigate', take_action=clue_actions.investigate_first_letter_action),
        ]