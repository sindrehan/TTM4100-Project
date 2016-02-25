# -*- coding: utf-8 -*-
import socket
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
        
        # TODO: Finish init process with necessary code
        self.history = 
        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        
    def disconnect(self):
        # TODO: Handle disconnection
        self.connection.close()

    def receive_message(self, message):
        # TODO: Handle incoming message
        response = MessageParser.parse()
        print response

    def send_payload(self, data):
        # TODO: Handle sending of a payload
        
        message = {"request": data, "content": }

        
    # More methods may be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
    print """Welcome to Chat9000. To log in, please enter: 'login <username>'

    To log out, please write 'logout'
    To exit, please write 'exit'
    """
    running = True
    while running:  
        raw = raw_input(":")
        if raw == "exit":
            running = False
        else:
            client.send_payload(raw)
