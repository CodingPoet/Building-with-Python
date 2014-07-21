from rooms.room import Room
from objects.door import Door

class Gardens(Room):
    
    def __init__(self):
        
        # the name of the room
        self.name = "Gardens"
        
        # a description of the room to show the user
        self.description = "The garden is overgrown, but looks as though it may have once been beautiful. There is a tool shed tucked behind a particularly large bush as the far end of the garden."
        
        # create all the doors leading out of the room
        self.doors = [
            Door('g', 'Glass Door', 'Dining Hall'),
            Door('s', 'Shed Door', 'Tool Shed', 'Key')
        ]
        
        # create all the items you can interact with in the room
        self.items = [
        ]

    
    
