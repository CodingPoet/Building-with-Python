import sys
import time
from rooms.room import Room
from rooms.alleyway import Alleyway
from rooms.kitchen import Kitchen
from rooms.dininghall import DiningHall
from rooms.gardens import Gardens
from rooms.cellar import Cellar
from rooms.toolshed import ToolShed
from objects.backpack import Backpack

class AdventureWorld(object):
	
	# this stuff happens as soon as the program is launched
	def __init__(self):
		
		print(sys.version)
		self.createRooms()
		self.backpack = Backpack()
		
	
	
	# create all the rooms in the game
	def createRooms(self):
		self.rooms = {
			'The Alleyway': Alleyway(),
			'Kitchen': Kitchen(),
			'Dining Hall': DiningHall(),
			'Cellar': Cellar(),
			'Gardens': Gardens(),
			'Tool Shed': ToolShed()
		}
	

	# start the game from the beginning
	def start(self):
		
		print("")
		print("Welcome to my Adventure Game")
		print("You wake to find yourself in a dark, dirty alleyway. Night is falling. Your head hurts and you can't remember how you got here. ")
		print("")
		
		self.enterRoom("The Alleyway")


	# enter a specific room
	def enterRoom(self, roomName):

		room = self.rooms[roomName]

		# describe the room
		print("")
		print(room.name)
		print(room.description)
		print("")
		
		if room.name == "Tool Shed":
			self.end()
		else:
			self.askWhatToDo(room)
	

	# ask the user what they want to do next	
	def askWhatToDo(self, room):
		
		# print out the options
		print("Options:")
		
		# list the door options
		for door in room.doors:
			print ("[" + door.button + "] " + door.name)
		
		# list the item options 
		for item in room.items:
			print ("[" + item.button + "] " + item.name)
		
		# ask the user to make a choice
		print("")
		buttonPressed = input("What next? ")
		
		print("")
		print("-----------------")
		print("")
		
		# try to find a door associated with that key
		chosenDoor = room.getDoorByButton(buttonPressed)
		
		# try to find an item associated with that key
		chosenItem = room.getItemByButton(buttonPressed)
		
		# act based on the door or item selected
		if chosenDoor != None:
			self.openDoor(chosenDoor, room)		
		elif chosenItem != None:
			self.takeItem(chosenItem, room)
			self.askWhatToDo(room)
		else:
			print('That key is not valid')
			time.sleep(1.5)
			self.askWhatToDo(room)
	
	
	# try to open the chosen door
	def openDoor(self, door, room):
		
		if door.requiredItem == None:	
			self.enterRoom(door.leadsTo)
		else:
			item = self.backpack.getItem(door.requiredItem)
			
			if item != None:
				print("Used " + item.name)
				time.sleep(1.5)
				self.enterRoom(door.leadsTo)
			else:
				print("It looks like you need a " + door.requiredItem)
				print("")
				time.sleep(1.5)
				self.askWhatToDo(room)
			
			
	
	
	# add an item to your backpack	
	def takeItem(self, item, room):
		room.removeItem(item)
		self.backpack.items.append(item)
		print('Added ' + item.name + ' to inventory.')
		print('')
		time.sleep(1.5)
		


	# end the game
	def end(self):
		print("Thanks for playing!")
		playagain = input("Play again? (y/n)")
		
		if playagain is "y":
			self.start()
		else:
			sys.exit()

	

