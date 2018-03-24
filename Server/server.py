import socketserver
import socket
import threading
import json

from client import *

# class ThreadedTCPHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         data = self.request.recv(1024).decode('utf-8')
#         data = json.loads(data)
#         cur_thread = threading.current_thread()
#         response = bytes("{}: {}".format(cur_thread.name, data['type']),'utf-8')
#         self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def tmpClient(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        message = json.dumps(message)
        sock.sendall(bytes(message,'utf-8'))
        response = sock.recv(1024).decode('utf-8')
        print("Received: {}".format(response))
    finally:
        sock.close()

if __name__ == "__main__":
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST,PORT), ClientTCPHandler)
    ip, port = server.server_address

    # start a thread with the server (start one more thread for each request)

    server_thread = threading.Thread(target=server.serve_forever)

    # exit when main thread ends

    server_thread.daemon = True
    server_thread.start()

    fMessage = {"type":"CONNECT","data":"Nkxs"}
    sMessage = {"type":"CONNECTE","data":"Ouii"}

    tmpClient(ip, port, fMessage)
    tmpClient(ip, port, sMessage)

    server.shutdown()