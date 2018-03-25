import apiai
import json
import os
import sys

from threading import Thread

from flask import Flask, render_template
from flask import request
from flask import make_response
from flask_socketio import SocketIO
from flask_socketio import send, emit

from game import *
from utils_func import *

app = Flask(__name__)
socketio = SocketIO(app)

CLIENT_ACCESS_TOKEN = '1724fbe91e264afdb2274fe6e5cf3226'
SUITCASE = 0
WOULD_YOU_RATHER = 1
COLLECTIVE = 2

state = State.WAIT_PLAYERS
game = Game()

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))

    res = process(req)
    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def process(req):
    global state
    speech = ""
    intent = req["result"]["metadata"]["intentName"]

    if state == State.WAIT_PLAYERS and intent == "start_playing":
        print("STATE: WAIT PLAYERS")
        speech = "Say next game to start a round." + str(state)
        state = State.WAIT_NEW_ROUND
        print("PASSING IN STATE: WAIT PLAYERS")

    elif state == State.WAIT_NEW_ROUND and intent == "next_game":
        print("STATE: WAIT NEW ROUND")
        speech = "A new round of the game Would You Rather will start!" + str(state)
        choice = pick_wyr_array()
        # Save choices
        game.update_wyr_choice(choice[0], choice[1])

        speech += " Would you rather " + choice[0] + " or " + choice[1] + str(state)

        # Sends choices to client
        socketio.emit('wyr_ask', {"A": choice[0], "B": choice[1]})

        state = State.WYR_WAIT
        print("PASSING IN STATE: WYR WAIT")

    elif state == State.WYR_WAIT and intent == "round_end":
        print("STATE: WAIT WYR WAIT")

        speech = game.get_wyr_answer()
        speech += " Punishment for all losers: " + get_gage()
        speech += " Say next round to start a new round." + str(state)
        state = State.WAIT_NEW_ROUND
        print("PASSING IN STATE: NEW ROUND")

    else:
        speech = "Query not understood."

    return {
        "speech": speech,
        "displayText": speech
    }


@socketio.on('connect')
def connect():
    global game
    # add a client
    print("New client!!!")
    id = request.sid
    socket = request.namespace
    p = Player(id, socket, "", [])
    game.add_player(p, id)


@socketio.on('info')
def info(json):
    global game
    print("Information from client : " + str(json))
    id = request.sid
    game.players[id].name = json["name"]


@socketio.on('wyr_answer')
def wyr_answer(json):
    # handle response to WYR game
    id = request.sid

    data = json.loads(json)
    answer = data["answer"]
    print("received ", answer)
    game.add_wyr_answer(answer)

@socketio.on('team_answer')
def team_answer(json):
    # handle team answer
    id = request.sid
    data = json.loads(json)


@socketio.on('story_answer')
def story_answer(json):
    # handle story answer
    id = request.sid
    data = json.loads(json)


def start_game():
    print("Game started")


if __name__ == '__main__':
    t = Thread(target=start_game, args=())
    t.start()
    socketio.run(app)
    t.join()
