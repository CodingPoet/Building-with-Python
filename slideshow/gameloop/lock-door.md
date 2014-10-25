### Lock Door

In `gardens.py`, modify the Shed Door:

	# create all the doors leading out of the room
    self.doors = [
        Door("g", "Glass Door", "Dining Hall"),
        Door("s", "Shed Door", "Tool Shed", "Key")
    ]

Note:
We want to lock the door from the garden side, so in `gardens.py` we need to add a required item to the tool shed door.

Take a look at `Door.py` to see how the `requiredItem` parameter is optional.

The item name we add needs to exactly match the name of the item we added to the cellar.