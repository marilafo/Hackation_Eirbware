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

    #res = processRequest(req)
    res = process(req)
    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):

    speech = ""

    # Processes intent
    intent = req["result"]["metadata"]["intentName"]

    if intent == 'start_playing' or intent == 'next_game':
        action = getAction()
        speech = processAction(action)

    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
    }

def getAction():
    # TODO query server to get the next action
    return [1, 1, "Eat a pizza", "Get some sleep"]

def processAction(action):
    code = action.pop(0)

    # Game
    if code == 1:
        game = action.pop(0)

        if game == WOULD_YOU_RATHER:
            a = action.pop(0)
            b = action.pop(0)
            return "Would you rather " + a + " or " + b + "?"

        if game == SUITCASE:
            # TODO treat parameters
            return "In my suitcase there is..."

        if game == COLLECTIVE:
            # TODO treat parameters
            return "Collective game"

    elif code == 2:
        return "Gage"

    else:
        return "Eat pizza"


def process(req):
    global state
    speech = ""
    intent = req["result"]["metadata"]["intentName"]

    if state == State.WAIT_PLAYERS and intent == "start_playing":
        speech = "Say next game to start a round." + str(state)
        state = State.WAIT_NEW_ROUND
    elif state == State.WAIT_NEW_ROUND and intent == "next_game":
        speech = "A new round of the game Would You Rather will start!" + str(state)
        choice = pick_wyr_array()
        speech += "What would you prefer between" + choice[0] + " and " + choice[1] + str(state)
        emit('wyr_ask', None)
        state = State.WYR_WAIT
    elif state == State.WYR_WAIT and intent == "round_end":
        speech = "Losers are John and Levin."
        speech += "Say next round to start a new round." + str(state)
        state = State.WAIT_NEW_ROUND
    else:
        speech = "Query not understood."

    return {
        "speech": speech,
        "displayText": speech
    }


@socketio.on('connect')
def connect(json):
    global game
    # add a client
    id = request.namespace.socket.sessid
    data = json.loads(json)
    socket = request.namespace
    p = Player(id, socket, "test", [])
    game.add_player(p, id)


@socketio.on('wyr_answer')
def wyr_answer(json):
    # handle response to tp game
    id = request.namespace.socket.sessid
    data = json.loads(json)


@socketio.on('team_answer')
def team_answer(json):
    # handle team answer
    id = request.namespace.socket.sessid
    data = json.loads(json)


@socketio.on('story_answer')
def story_answer(json):
    # handle story answer
    id = request.namespace.socket.sessid
    data = json.loads(json)


def start_game():
    print("Game started")


if __name__ == '__main__':
    t = Thread(target=start_game, args=())
    t.start()
    socketio.run(app)
    t.join()
