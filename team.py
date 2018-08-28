
class Team:
    hands_won = 0
    players = list()
    games_won = 0

    def __init__(self, player1, player2):
        self.players.append(player1)
        self.players.append(player2)