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
        for row in self.cards:
            s = ""
            for card in row:
                s += card.get_value()
                s += " "
            print(s)
