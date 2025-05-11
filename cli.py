import re
from game import Game

class CLI:
    def __init__(self):
        print("Hi there, it's Memory game written in Python.\nType 'help' to check commands\n")
        self.commands = ["help", "game", "saved_games", "exit"]
        self.running = True
    
    def run(self):
        while self.running:
            command = self.handle_input()
            self.handle_command(command)


    def handle_input(self):
        command = None
        is_valid = False
        while not is_valid:
            command = input()
            command = command.strip(" \n")
            is_valid = self.check_if_valid(command)
        return command
        

    def check_if_valid(self, value):
        if value in self.commands:
            return True
        else:
            print("Wrong input, try again")
            return False 

    
    def show_help(self):
        print('''
        You can you following commands:
            help - to open this manual 
            game - to start new game
            saved_games - to look saved games
            exit - to exit 
        ''')
        
    def start_game(self):
        players_num = None 
        while not players_num:
            players_num = input("Enter number of players (1 - 9):\n").strip(' \n')
            if not re.fullmatch(r'\d', players_num):
                print("Wrong number of players")
                players_num = None
        
        Game(int(players_num)).run()
        print("Type 'game' to start new game")

    
    def show_saved_games(self):
        pass

    def handle_command(self, command):
        match command:
            case 'help':
                self.show_help()
            case 'game':
                self.start_game()
            case 'exit':
                self.running = False
            case 'saved_games':
                self.show_saved_games()
            

