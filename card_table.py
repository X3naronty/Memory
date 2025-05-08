
class Card_table:
	def __init__(self):
		self.cols, self.rows = 4, 4
		self.active_cards = self.get_active_cards()

	def get_active_cards(self):
		return [[Card() * ] * self.rows]

	def draw(self):
		pass