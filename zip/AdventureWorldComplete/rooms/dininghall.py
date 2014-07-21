from rooms.room import Room
from objects.door import Door

class DiningHall(Room):
    
    def __init__(self):
        
        # the name of the room
        self.name = "Dining Hall"
        
        # a description of the room to show the user
        self.description = "The room looks like it hasn't been touched for years. There are plates still set out around the table, with what looks like the remnants of an ancient meal shared around."
        
        # create all the doors leading out of the room
        self.doors = [
            Door('a', 'Air Vent', 'Alleyway'),
            Door('b', 'Brown Door', 'Kitchen'),
            Door('g', 'Glass Door', 'Gardens')
        ]
        
        # create all the items you can interact with in the room
        self.items = []
    
    
