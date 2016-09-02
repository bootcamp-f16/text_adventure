
class Room():
    def __init__(self,
        name="",
        description="",
        monster=None,
        items=None):
        
        self.name = name
        self.description = description
        self.monster = monster
        self.items = items or []

def rooms_builder():
    """
    Returns a starting room that contains
    a tree of rooms off the starting room
    """
    
    starting_room = Room(
        name="Starting Point",
        description="This is the first room")

    #TODO: build tree of rooms off of starting room

    return starting_room