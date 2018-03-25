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
SUITCASE = 0
WOULD_YOU_RATHER = 1
COLLECTIVE = 2

def sendEvent():
    print("event")
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    event = apiai.events.Event("PLAYER_JOINED")
    request = ai.event_request(event)

    request.lang = 'en'
    request.session_id = "iefifhufhjfndsiff"

    response = request.getresponse()
    print (response.read())


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))

    res = processRequest(req)
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


def start_game():
    print("Game started")


if __name__ == '__main__':

    p = Process(target=start_game, args=())
    p.start()
    app.run(debug=True, use_reloader=False)
    p.join()
