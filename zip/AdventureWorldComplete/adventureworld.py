import sys

class AdventureWorld(object):
	
	# this stuff happens as soon as the program is launched
	def __init__(self):
		
		print(sys.version)
	

	# start the game from the beginning
	def start(self):
		
		print("")
		print("Welcome to my Adventure Game")
		print("You wake to find yourself in a dark, dirty alleyway. Night is falling. Your head hurts and you can't remember how you got here. ")
		print("")


	# end the game
	def end(self):
		
		print("Thanks for playing!")
		playagain = input("Play again? (y/n)")
		
		if playagain is "y":
			self.start()
		else:
			sys.exit()

	

