---
title: item-by-button
section: gameloop
layout: slide
class: default-slide

notes: |
  And just as we look up doors by the button the user pressed, we can look up items too.

---


### Item By Button

	# try to find a door associated with that button
	chosenDoor = room.getDoorByButton(buttonPressed)
		
	# try to find an item associated with that button
	chosenItem = room.getItemByButton(buttonPressed)
