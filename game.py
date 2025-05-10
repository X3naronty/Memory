import os
import time
from card_table import Card_table
import re


class Game:
    def __init__(self):
        # self.players = []
        # self.player = self.players[0]
        self.states = ["making_first_rush", "making_second_rush"]
        self.state = self.states[0]
        self.card_table = Card_table()

    def run(self):
        while True:
            self.draw()
            try:
                self.handle_input()
            except ValueError as e:
                print(e)
                time.sleep(2)
                continue

            # first_card = self.get_card(self.handle_input("Write here row and column with space\n"))
            # self.update(first_card)
            # self.draw()
            # second_card = self.get_card(self.handle_input("Write here row and column with space\n"))
            # self.update(second_card)
            # self.draw()
            # time.sleep(1.5)
            # is_equal = self.handle_result(first_card, second_card)
            # if not is_equal: self.update(first_card, second_card)

    def get_card(self, coords: tuple[int, int]) -> object:
        row, col = coords
        return self.card_table.cards[row][col - 1]

    def fetch_data(self, value) -> tuple[int, int]:
        value = re.sub(r'\s+', ' ', value.strip(" \n"))
        if re.fullmatch(r'\d+ \d+', value):
            row, col = map(int, value.split())
        else:
            raise ValueError('Wrong input, try again')

        if row > self.card_table.rows or col > self.card_table.cols or row == 0 or col == 0:
            raise ValueError('Wrong input, try again')

        return row - 1, col - 1

    def handle_input(self):
        # message = f"Player's {self.player.name} turn. Enter card's row and column by space:"
        message = 'Enter 2 numbers by space\n'
        value = input(message)

        first_card = self.get_card(self.fetch_data(value))
        first_card.flip()
        self.draw()
        
        value = input(message)
        second_card = self.get_card(self.fetch_data(value))
        second_card.flip()
        self.draw()
        
        if first_card.value == second_card.value:
            # self.player.score += 1
            first_card.make_inactive()
            second_card.make_inactive()
            
        else:
            time.sleep(1.5)
            first_card.flip()
            second_card.flip()



    # def handle_input(self, message) -> tuple[int, int]:
    #     card_position = input(f"{message}");
    #     card = tuple(map(lambda x: int(x), card_position.split(' ')));
    #     return card

    def update(self, *cards):
        for card in cards:
            if card.is_active:
                card.flip()
            else:
                print("Choose another card")

    def handle_result(self, first_card, second_card) -> bool:
        if first_card.value == second_card.value:
            # self.player.score += 1
            first_card.make_inactive()
            second_card.make_inactive()
            return True

    def draw(self):
        os.system('clear')
        self.card_table.draw()
