from rooms.room import Room
from objects.door import Door

class Kitchen(Room):
    
    def __init__(self):
        
        # the name of the room
        self.name = "Kitchen"
        
        # a description of the room to show the user
        self.description = "You stand in a small kitchen. A large black rat looks up at you. There are unwashed dishes in the sink. You can't wait to get out of here."
        
        # create all the doors leading out of the room    
        self.doors = [
            Door("r", "Red Door", "Alleyway"),
            Door("b", "Brown Door", "Dining Hall"),
            Door("w", "Wooden Door", "Cellar")
        ]
        
        # create all the items you can interact with in the room
        self.items = []
    
