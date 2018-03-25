import random


choose_array = [
    ["Harry Potter", "Twilight"],
    ["Do the Hunger Game", "Be throw in the Maze Runner"],
    ["Exprim yourself only vith vowel", "Exprim yourself only with consonant"],
    ["Have a bad plates everytime you go to restaurant", "Arrive at the wrong place when you go oon trip"]
]

gage_array = [
    "You have to do 1 push-up",
    "You have to do 2 push-up",
    "You have to do 3 push-up",
    "You have to do 4 push-up",
    "You have to do 5 push-up"
]

collective_array = [
    "You have to run over the table and do 1 turn",
    "You have to run over the table and do 2 turn",
    "You have to run over the table and do 3 turn",
    "You have to run over the table and do 4 turn",
    "You have to run over the table and do 5 turn",
    "You have to run over the table and do 6 turn"
]

class Player(object):

    def __init__(self, name, clues, socket):
        self.socket = socket
        self.name = name
        self.clues = clues
        self.story_clues = []
        self.team_clues = []
        self.team_found = False

    def set_team(self, team):
        self.team = team

    def get_team(self):
        return self.team

    def check_team(self, team):
        if self.team == team:
            self.team_found = True
            return True
        else:
            return False
    
    def team_ready(self, players):
        return self.team_found and players[self.team]

    def add_story(self, clue):
        self.story_clues.append(clue)
    
    def get_story(self):
        return self.story_clues

    def add_team(self, clue):
        self.team_clues.append(clue)
    
    def get_teams(self):
        return self.team_clues

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id


class State():
    WAIT_PLAYERS = 0
    START_GAME = 1
    CHOOSE_TEAM = 2



class Game(object):
    def __init__(self):
        self.nb_turn = 0
        self.nb_player = 0
        self.players = []
    
    def add_player(self, player):
        player.id = self.nb_player
        self.players.append(player)

    def 
    




