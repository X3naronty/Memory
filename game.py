import os
import time
from card_table import Card_table
import re
import sys
import select
from player import Player
from collections import deque
from datetime import datetime
import pickle

def flush_stdin():
    while select.select([sys.stdin], [], [], 0)[0]:
        sys.stdin.readline()

class Game:
    def __init__(self, players_num):
        print("If you want to save the game, type 'save'")
        self.players = deque([Player() for i in range(players_num)])
        self.card_table = Card_table()
        self.open_cards_count = 0
        self.is_running = True
    
    @property
    def player(self):
        return self.players[0]
    
    def change_player(self):
        self.players.rotate(-1)

    def run(self):
        while self.is_running:
            self.draw()

            first_card = None
            while not first_card:
                first_card = self.handle_input(1)
                self.draw()

            second_card = None 
            while not second_card:
                second_card = self.handle_input(2)
                self.draw()

            self.handle_result(first_card, second_card)

    def get_card(self, coords: tuple[int, int]) -> object:
        row, col = coords
        print(row, col)
        if row > self.card_table.rows or col > self.card_table.cols or row < 0 or col < 0:
            raise ValueError('Wrong input, try again')
        return self.card_table.cards[row][col]

    def fetch_input(self, value) -> tuple[int, int]:
        # strip spaces
        value = re.sub(r'\s+', ' ', value.strip(" \n"))

        if re.fullmatch(r'\d+ \d+', value):
            return value
        elif value == "save":
            return value 
        else:
            raise ValueError('Wrong input, try again')

    def handle_card(self, value):
        try:
            card = self.get_card(tuple(map(lambda x: int(x) - 1, value.split())))
            card.flip('up')
            return card
        except ValueError as e:
            print(e)
            time.sleep(2)
            flush_stdin()
            return None
    
    def save_game(self):
        date = str(datetime.now())
        value = input(f"Enter the name of your game.\n Press enter to set default({date})\n")
        value = value.strip(' \n') 

        name = value if value else date
        
        with open(f'./saved_games/{name}.pickle', "wb") as f:
            pickle.dump(self, f)
            print("Successfully saved)")


    def handle_input(self, num):
        message = f"""Player_{self.player.count}'s {num} rush.
Type 'quit' to quit the game
Type 'save' to save the game
Enter card's row and column by space:\n"""
        # message = 'Enter 2 numbers by space\n'
        value = input(message)
                
        value = self.fetch_input(value)
        
        match value: 
            case "save":
                self.save_game()
            case _:
                return self.handle_card(value)

        return None

        
        
    def handle_result(self, first_card, second_card):    
        if first_card.value == second_card.value:
            self.player.score += 1
            first_card.make_inactive()
            second_card.make_inactive()
            
            self.open_cards_count += 2
            if self.open_cards_count == self.card_table.rows * self.card_table.cols:
                for player in self.players:
                    print(f"Player_{player.count} score: {player.score}")
                self.is_running = False
            

            time.sleep(1.5)
            flush_stdin()
        else:
            time.sleep(1.5)
            flush_stdin()
            first_card.flip('down')
            second_card.flip('down')
            self.change_player()

    def draw(self):
        os.system('clear')
        self.card_table.draw()
        
