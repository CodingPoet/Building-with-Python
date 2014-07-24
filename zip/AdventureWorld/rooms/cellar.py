from rooms.room import Room
from objects.door import Door
from objects.item import Item

class Cellar(Room):
    
    def __init__(self):
        
        # the name of the room
        self.name = "Cellar"
        
        # a description of the room to show the user
        self.description = "The cellar is grimy. There are a few old bottles of wine lying around, most broken. There are no other exits."
        
        # create all the doors leading out of the room
        self.doors = [
            Door("s", "Stairwell Door", "Kitchen"),
        ]
        
        # create all the items you can interact with in the room
        self.items = [
        ]
    
