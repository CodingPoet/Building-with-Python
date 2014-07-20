import objects.player
from objects.room import Room

class AdventureWorld:

	def __init__(self):
		self.player = Player()
		self.rooms = []

	def introduction(self):

		print("Welcome to my game")
		self.name = raw_input("What is your character's name? ")