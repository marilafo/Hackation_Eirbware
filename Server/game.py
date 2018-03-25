import random


choose_array = [
        ["Watch Harry Potter", "Watch Twilight"],
        ["Do the Hunger Game", "Be throw in the Maze Runner"],
        ["Exprim yourself only vith vowel", "Exprim yourself only with consonant"],
        ["Have a bad plates everytime you go to restaurant", "Arrive at the wrong place when you go on a trip"]
    ]

gage_array = [
        ["You have to do 1 push-up"],
        ["You have to do 2 push-up"],
        ["You have to do 3 push-up"],
        ["You have to do 4 push-up"],
        ["You have to do 5 push-up"]
        ]

collective_array = [
        ["You have to run over the table and do 1 turn"],
        ["You have to run over the table and do 2 turn"],
        ["You have to run over the table and do 3 turn"],
        ["You have to run over the table and do 4 turn"],
        ["You have to run over the table and do 5 turn"],
        ["You have to run over the table and do 6 turn"]
        ]

clues_pair_array = [
        ["Clue pair 1"],
        ["Clue pair 2"],
        ["Clue pair 3"],
        ["Clue pair 4"],
        ["Clue pair 5"]
        ]

clues_investigation_array = [
        ["Clue investigation 1"],
        ["Clue investigation 2"],
        ["Clue investigation 3"],
        ["Clue investigation 4"],
        ["Clue investigation 5"],
        ["Clue investigation 6"],
        ]


Class Player(object):
    id = 0
    clues = []
    name = ""
    find_pair = False

    clues_pair = []
    clues_investigation = []

    def __init__(seld, id, clues_list, name):
        self.id = id
        self.clues = clues_list
        self.name = name
        for i in range(clues_pair_array):
            clues_pair.append(0)
        for i in range(clues_investigation_array):
            clues_investigation.append(0)

    def set_pairs(self, player_pair)
        self.pair = player_pair

    def get_name(self):
        return self.name

    def have_pair(self):
        return self.find_pair

    def is_pair(self, i):
        return self.pair == i

    def have_pair_clue(self, i):
        return self.clues_pair[i] != 0:

    def have_investigation_clue(self, i):
        return self.clues_investigation[i] != 0

    def set_pair_clue(self, i):
        self.clues_pair[i] = 1

    def set_investigation_clue(self, i):
        self.clues_investigation[i] = 1


Class Game(object):
    nb_turn = 0
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
        send_to_master([0])


    def run_suitcase(self, players_array):
        l_to_send = [2,0]
        looser = []
        send_to_master([1,0])
        #TODO Nicolas call
        s = get_answer()
        for p in players_array:
            if p.get_name() == s:
                l_to_send.append(p.get_name())
                looser.append(p)

        gage = random.randrange(0,len(gage_array))
        l_to_send.append(gage_array[gage])
        send_to_master(l_to_send)
        return looser


    def run_choose(self, players_array):
        l_to_send=[2,1]
        looser = []
        c = random.randrange(0, len(choose_array))

        send_to_master_client([1,1,choose_array[c][0], choose_array[c][1]])
        #TODO Nicolas
        answer_lists = getChooseAnswer()
        up = answer_lists.count("up")
        down = answer_lists.count("down")

        best = 0
        if up > down:
            best = 1
        elif up == downi:
            best = -1
        for i in range(0,len(answer_lists)):
            if answer_list[i] == "up":
                if best == 0 or best == -1:
                    l_to_send.append(players_array[i].get_name())
                    looser.append(players_array[i])

            else :
                if best == 1 or best == -1:
                    l_to_send.append(players_array[i].get_name())
                    looser.append(players_array[i])

        gage = random.randrange(0,len(gage_array))
        l_to_send.append(gage_array[gage])


        if best == 1:
            l_to_send.insert(0, 2)
            l_to_send.insert(choose_array[c][0], 3)
            send_to_master(l_to_send)
        elif best == 0:
            l_to_send.insert(0,2)
            l_to_send.insert(choose_array[c][1], 3)
            send_to_master(l_to_send)

        elif best == -1:
            l_to_send.insert(1,2)
            send_to_master(l_to_send)

        return looser



    def run_collective(self, players_array)
        looser = []
        l_to_send = [2,2]

        action = random.randrange(0,len(collective_array))


        send_to_master([1,2, collective_array[action]])
        #TODO Nicolas call
        s = get_answer()
        for p in players_array:
            if p.get_name() == s:
                l_to_send.append(p.get_name())
                looser.append(p)


        gage = random.randrange(0,len(gage_array))
        l_to_send.append(gage_array[gage])

        send_to_master(l_to_send)
        return looser

    def send_pair_clue(self, player):
        clue = random.randrange(0, len(clues_pair_array))
        for i in len(clues_pair_array)*2:
            if player.have_clue(clue):
                clue = random.randrange(0, len(clues_pair_array))
            else:
                send_client(clues_pair_array[clue])
                player.set_pair_clue(clue)
                return



    def send_investigation_clue(self, player):
        clue = random.randrange(0, len(clues_investigation_array))

        for i in len(clues_investigation_array)*2:
            if player.have_clue(clue):
                clue = random.randrange(0, len(clues_investigation_array))
            else:
                send_client(clues_investigation_array[clue])
                player.set_investigation_clue(clue)
                return



    def run_turn(self, players_array):
            looser = random.randrange(0, 3)
        if mini_game == 0:
            looser = self.run_suitcase(players_array)
        elif mini_game == 1:
            looser = self.run_choose(players_array)
        elif mini_game == 2:
            looser = self.run_collective(players_array)

        for p in players_array:
            if p not in looser:
                if self.nb_turn == 0:

                    if not p.have_pair():
                        self.send_pair_clue(p)
                    else
                        self.send_investigation_clue(p)
                else:
                    self.send_investigation_clue(p)

        self.nb_turn = self.nb_turn + 1


    #def ask_pair(self, players_array):
    #    for p in players_array:



    #def ask_solution(self, players_array):
    #    for p in players_array:
    #        if





    def start_game(self, players_array):
        self.nb_turn = 0
        random.seed()
        self.select_pairs(players_array)

        #self.display_history()

        end = False

        while not end:
            if (self.nb_turn == 3):
                self.ask_pair(players_array)
            elif (self.nb_turn == 5):
                self.ask_solution(players_array)
            end = self.run_turn(players_array)
