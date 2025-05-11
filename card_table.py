from card import Card
import random


class Card_table:
    def __init__(self):
        self.cols, self.rows = 4, 4
        self.card_values = ["#", "#", "$", "$", "@", "@",
                            "%", "%", "~", "~", "*", "*", "+", "+", ")", ")"]
        self.cards: list[list][str] = self.get_cards()

    def get_cards(self):
        return [[Card(self.get_card_value(), j, i) for i in range(self.cols)] for j in range(self.rows)]

    def get_card_value(self):
        item = self.card_values.pop(random.randrange(len(self.card_values)))
        return item

    def draw(self):
        for row in range(self.rows + 1):
            s = ""
            for col in range(self.cols + 1):
                if row > 0 and col > 0:
                    card = self.cards[row - 1][col - 1]
                    s += card.get_value()
                elif row == 0 and col:
                    s += str(col)
                elif col == 0 and row:
                    s += str(row)
                else: 
                    s += '$'
                s += " "
            print(s)
