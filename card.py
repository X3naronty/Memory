
class Card:
    def __init__(self, value, row, col):
        self.state = "down"
        self.value = value
        self.is_active = True
        self.row = row
        self.col = col

    def get_value(self):
        return self.value if self.state == "up" else '?'

    def make_inactive(self):
        self.is_active = False

    # up down
    def flip(self, new_state):
        if self.is_active and self.state != new_state:
            self.state = new_state
        else:
            raise ValueError("You can't choose open this card")
