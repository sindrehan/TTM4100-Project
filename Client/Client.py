# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """
        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.server_port = server_port
        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        worker = MessageReceiver(self, self.connection)
        worker.daemon = True
        worker.start()
        running = True
        while running:
            raw = raw_input()
            if raw == "exit":
                running = False
                self.disconnect()
            else:
                self.send_payload(raw)
    def disconnect(self):
        self.connection.close()

    def receive_message(self, message):
        #print message
        parser = MessageParser()
        response = parser.parse(message)
        print response
    def send_payload(self, data):
        message = {"request": data.partition(' ')[0],\
                   "content": data.partition(' ')[2] }
        self.connection.sendall(json.dumps(message))

if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    print """Welcome to Chat9000. To log in, please enter: 'login <username>'

    To log out, please write 'logout'
    To exit, please write 'exit'
    """
    client = Client('localhost', 9998)
