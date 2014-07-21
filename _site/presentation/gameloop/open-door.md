### Open Door

	# try to open the chosen door
	def openDoor(self, door, room):
		
		if door.requiredItem == None:	
			self.enterRoom(door.leadsTo)
		else:
			item = self.backpack.getItem(door.requiredItem)
			
			if item != None:
				print("Used " + item.name)
				self.enterRoom(door.leadsTo)
			else:
				print("It looks like you need a " + door.requiredItem)
				self.askWhatToDo(room)

Note:
If the door has no required item, we can enter the room without trouble.

Otherwise... try to get the required item from our backpack.

If we have the item, use it, and enter the room.

If we don't have the item, print an error and ask the user what to do next.

Play your game again. Can you open the locked door without the item?

Once you pick up the key, can you then open the door?