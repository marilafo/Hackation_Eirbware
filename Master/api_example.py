import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '1724fbe91e264afdb2274fe6e5cf3226'

def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    event = apiai.events.Event("WOULD_YOU_RATHER")

    request = ai.event_request(event)
    
    request.lang = 'en'
    request.session_id = "iefifhufhjfndsiff"

    response = request.getresponse()

    print (response.read())


if __name__ == '__main__':
    main()