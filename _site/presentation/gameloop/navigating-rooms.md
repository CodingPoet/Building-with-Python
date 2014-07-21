### Navigating Rooms

	# try to find a door associated with that button
	chosenDoor = room.getDoorByButton(buttonPressed)

    self.enterRoom(chosenDoor.leadsTo)

Note:
Now that all our rooms are set up, we should be able to navigate between them.

After your player has pressed a key, find the room associated with that key and enter the room.

