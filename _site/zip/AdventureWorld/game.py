from adventureworld import AdventureWorld

class Game(object):
	
	def run(self):
		self.game = AdventureWorld()
		self.game.start()

# This is the starting point for our whole app
if __name__ == "__main__":
	app = Game()
	app.run()