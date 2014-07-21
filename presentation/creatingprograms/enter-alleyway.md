### Enter Alleyway

    def start(self):
		
		print("")
		print("Welcome to my Adventure Game")
		print("You wake to find yourself in a dark, dirty alleyway. Night is falling. Your head hurts and you can't remember how you got here. ")
		print("")
		
		room = self.rooms['Alleyway']
		print(room.name)
		print(room.description)

Note:
Now we need to have the player actually enter the alleyway.

Find your game introduction text, in the main `adventureworld.py` file.

Underneath your introduction, we want to get the information about the Alleyway and print it our for the user.

Run the game to check that it works!