---
title: navigating-rooms
section: gameloop
layout: slide
class: default-slide

notes: |
  Now that all our rooms are set up, we should be able to navigate between them.

  After your player has pressed a button, find the room associated with that button and enter the room.

---

### Navigating Rooms

	# try to find a door associated with that button
	chosenDoor = room.getDoorByButton(buttonPressed)

    self.enterRoom(chosenDoor.leadsTo)

