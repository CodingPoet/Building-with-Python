from rooms.room import Room
from objects.door import Door

class ToolShed(Room):
    
    def __init__(self):
        
        # the name of the room
        self.name = "Tool Shed"
        
        # a description of the room to show the user
        self.description = "You rummage around the tool shed and find a rocket pack! Awesome! You can finally escape this crazy place and find your way home."
        
        # create all the doors leading out of the room    
        self.doors = [
            Door('s', 'Shed Door', 'Gardens')
        ]
        
        # create all the items you can interact with in the room
        self.items = []
