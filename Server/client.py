from collections import defaultdict

import socketserver
import socket
import threading
import json

CLIENT_PSIZE = 2048
CLIENT_LIST = []

def log(message):
    print(message + '\n')

def connect(data):
    log("Client successfully connected !")

def teamAnswer(data):
    return

def storyAnswer(data):
    return

def tpAnswer(data):
    return

def actionError():
    print("Incorrect keyword")
    return

class ClientTCPHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        while True:    
            # {'type'='state','data'={...}}
            received_data = json.loads(self.request.recv(CLIENT_PSIZE).decode('utf-8'))
            d = received_data['data']
            states = {
                'CONNECT': connect(d),
                'TEAM_ANSWER': teamAnswer(d),
                'STORY_ANSWER': storyAnswer(d),
                'TP_ANSWER': tpAnswer(d),
            }
            states = defaultdict(actionError(), states)
            states[received_data['type']]
        
    def getChooseAnswer():
        