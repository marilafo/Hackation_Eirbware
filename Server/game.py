import random


choose_array = [
        ["Harry Potter", "Twilight"],
        ["Do the Hunger Game", "Be throw in the Maze Runner"],
        ["Exprim yourself only vith vowel", "Exprim yourself only with consonant"],
        ["Have a bad plates everytime you go to restaurant", "Arrive at the wrong place when you go oon trip"]
        ]


Class Player:
    id = 0
    clues = []
    name = ""

    def __init__(seld, id, clues_list, name):
        self.id = id
        self.clues = clues_list
        self.name = name

    def set_pairs(self, player_pair)
        self.pair = player_pair

    def get_name(self):
        return self.name

Class Game:

    nb_player = 0
    player_array = []

    def __init__(self,  players_array):
        self.nb_player = len(players_array)
        self.players_array = players_array


    #TODO : verifier que le nombre de joueurs est pair
    def select_pairs(self, players_array):
        l = []
        num = 0
        for i in range(len(players_array)):
            l.append(num)
            num += 1

        while len(l) != 0:
            rand1 = random.randrange(0, len(l))
            rand2 = random.randrange(0, len(l))
            while rand1 == rand2:
                rand2 = random.randrange(0, len(l))

            p1 = l.pop(rand1)
            p2 = l.pop(rand2)
            
            players_array[p1].set_pairs(players_array[p2])
            players_array[p2].set_pairs(players_array[p1])
            

    def display_history(self):
        print("You are a detective ...'")
        

    def run_suitcase(self, players_array):
        looser = []
        print("Run suitcase game")
        s = get_answer()
        for p in players_array:
            if p.get_name() == s:
                  looser.append(p)
        return looser

    def run_choose(self, players_array):
        looser=[]
        c = random.randrange(0, len(choose_array))
    
        print("Run choose came %s, %s" % (choose_array[c][0], choose_array[c][1]))
        

    def run_turn(self, players_array):
        mini_game = random.randrange(0, 3)
        if mini_game == 0:
            self.run_suitcase()
        elif mini_game == 1:
            self.run_choose()
        elif mini_game == 2:
            self.run_collective()



    def start_game(self, players_array):
        random.seed()
        self.select_pairs(players_array)
            
        self.display_history()
        
        end = False

        while not end:
            end = self.run_turn(players_array)

            



