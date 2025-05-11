
class Player:
    count = 0
    def __init__(self):
        Player.count += 1
        self.count = Player.count
        self.score = 0
