### Take Item

	# add an item to your backpack	
	def takeItem(self, item, room):
		room.removeItem(item)
		self.backpack.items.append(item)
		print("Added " + item.name + " to backpack.")

Note:
Set up a function to remove the item from the room and put it in your backpack.