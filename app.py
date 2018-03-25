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

app = Flask(__name__)
socketio = SocketIO(app)

CLIENT_ACCESS_TOKEN = '1724fbe91e264afdb2274fe6e5cf3226'
WOULD_YOU_RATHER = 1


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print "coucou"
    print(json.dumps(req, indent=4))

    # Processes intent
    # intent =

    res = processRequest(req)
    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    speech = "Hey"
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
    }


def processAction(action):
    code = action.pop(0)
    # sendEvent()


    #if code == WOULD_YOU_RATHER:


@socketio.on('connect')
def connect(json):
    # add a client
    data = json.loads(json)


@socketio.on('team_answer')
def team_answer(json):
    # handle team answer
    data = json.loads(json)


@socketio.on('story_answer')
def story_answer(json):
    # handle story answer
    data = json.loads(json)


@socketio.on('tp_answer')
def tp_answer(json):
    # handle response to tp game
    data = json.loads(json)


def start_game():
    print("Game started")
    i = 0
    while(True):
        i += 1
        if i == 10000:
            print("ok" + i)


if __name__ == '__main__':
    t = Thread(target=start_game, args=())
    t.start()
    socketio.run(app)
    t.join()
