# -*- coding: utf-8 -*-
from threading import Thread
import sys

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and it allows
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """
        # Flag to run thread as a daemon
        super(MessageReceiver, self).__init__()
        self.daemon = True
        self.client = client
        self.connection = connection


    def run(self):
        while True:
            data = self.connection.recv(1024)
            if data:
                for message in data.split("\n"):
                    if message:
                        self.client.receive_message(message)
            else:
                sys.exit()
