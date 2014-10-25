### Respect Lock

Instead of just:

    # act based on the door or item selected
    if chosenDoor != None:
        self.enterRoom(chosenDoor.leadsTo)

We need to do:

    # act based on the door or item selected
    if chosenDoor != None:
        self.openDoor(chosenDoor, room)

Note:
It's not enough to just add a required item to the door. We need to actually check for that item when the player tried to enter the room.

If a door has a required item, we shouldn't be able to enter unless we have that item in our backpack.

To add in this functionality, we'll add an extra step before entering a room - "open door". At the end of the open door function, if we managed to open the door, we will _then_ enter the room.