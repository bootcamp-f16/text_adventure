from lib.actions import Action
import lib.npc_actions as npc_actions

class Npc():
    pass

class Overlord(Npc):
    def __init__(self):
        self.actions = [
            Action('talk', take_action=npc_actions.overlord_talk_action),
            Action('answer', take_action=npc_actions.overlord_answer_action),
        ]