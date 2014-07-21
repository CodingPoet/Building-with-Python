### Add alleyway to the game

Import `Alleyway` class at the top of `adventureworld.py`:

    import sys
    from rooms.alleyway import Alleyway

Add the Alleyway to the list of available rooms:

	def createRooms(self):
		self.rooms = {
			'The Alleyway': Alleyway()
		}

Note:
Let's make our game automatically put our player into the alleyway at the start of our game.

The first step is to add the alleyway to the list of rooms available in the game. Although we have a class which represents the alleyway, we haven't actually included it in our game yet.

Open up `adventureworld.py` and find the `createRooms` function.

You can see we already have a dictionary of room set up, but the dictionary is empty.

Start by adding the Alleyway to the rooms dictionary.

Try running your program to make sure there are no errors.
