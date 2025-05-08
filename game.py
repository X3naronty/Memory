
class Game:
	def __init__(self):
		self.players = []
		self.player = self.players[0]
		self.states = ["making_first_rush", "first_rush_done", "second_rush_done"]
		self.state = self.states[0]
		self.card_1 = None, None
		self.card_2 = None, None
	
	def run(self):
		while True:
			self.check_input()
			self.update()
			self.draw()
	
	def check_input(self):
		card_position = input(f"{self.player.name} rush:");
		self.card = tuple(map(lambda x: int(x), card_position.split(' ')));
	
	def update(self):
		card_table.update(self.card, self.state)
	
	def draw(self):
		card_table.draw()

		