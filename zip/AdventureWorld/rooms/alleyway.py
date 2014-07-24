from rooms.room import Room
from objects.door import Door

class Alleyway(Room):
    
    def __init__(self):
        
        # the name of the room
        self.name = "Alleyway"
        
        # a description of the room to show the user
        self.description = "The alleyway is dirty and slimy. You get a chill just standing here. There is a red door on the left side of the alley, a green door on the right, and a black spiked gate at one end."
        
        # create all the doors leading out of the room
        self.doors = [
            Door("r", "Red Door", "Kitchen"),
            Door("g", "Green Door", "Dining Hall"),
            Door("b", "Black Gate", "Gardens")
        ]
        
        # create all the items you can interact with in the room
        self.items = []
        
    