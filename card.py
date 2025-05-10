
class Card:
    def __init__(self, value, row, col):
        self.is_flipped = True
        self.value = value
        self.is_active = True
        self.row = row
        self.col = col

    def get_value(self):
        return self.value if not self.is_flipped else '?'

    def make_inactive(self):
        self.is_active = False

    def flip(self):
        if self.is_active:
            self.is_flipped = not self.is_flipped
        else:
            raise ValueError("This card is already opened")
