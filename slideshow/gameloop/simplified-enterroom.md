### Simplified enterRoom

	def enterRoom(self, roomName):
		
		room = self.rooms[roomName]
		print(room.name)
		print(room.description)
		
		if room.name == "Tool Shed":
			self.end()
		else:
			self.askWhatToDo(room)
		
Note:
After refactoring our code, it is much easier to see that after we enter a room, we print out its details and then if it's the tool shed end the game, otherwise ask the player what to do next.

Much tidier!