import apiai
import json
import os
import sys

from multiprocessing import Process

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

CLIENT_ACCESS_TOKEN = '1724fbe91e264afdb2274fe6e5cf3226'
WOULD_YOU_RATHER = 1

def sendEvent():
    print("event")
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    event = apiai.events.Event("PLAYER_JOINED")
    request = ai.event_request(event)

    request.lang = 'en'
    request.session_id = "iefifhufhjfndsiff"

    response = request.getresponse()
    print (response.read())
    return response.read()

@app.route('/webhook', methods=['POST'])
def webhook():
    sendEvent()
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    print(res)
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

    if code == WOULD_YOU_RATHER:


def start_game():
    print("Game started")
    sendEvent()


if __name__ == '__main__':
    print("hey")
    sendEvent()

    p = Process(target=start_game, args=())
    p.start()
    app.run(debug=True, use_reloader=False)
    p.join()

    print("coucou")
