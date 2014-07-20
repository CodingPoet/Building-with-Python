class Room(object):

	def __init__(self):
		pass
	

	# get the door object related to the key that was pressed
	def getDoorByButton(self, buttonPressed):

		chosenDoor = None
	
		for door in self.doors:

			if door.button is buttonPressed:
				chosenDoor = door
		
		return chosenDoor
		
	

