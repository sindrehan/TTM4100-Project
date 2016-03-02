# -*- coding: utf-8 -*-
import SocketServer
import json
import time

"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

messages = []
clients ={}
help_text = "GOod luck with your life, asshole!"

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        self.logged_in = False

        global messages
        global clients
        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)

            received = json.loads(received_string)
            client_request = received['request']
            content = received['content']

            if client_request == "login":
                if content in clients.values():
                    response = {'timestamp':time.strftime("%H:%M:%S"),
                                'sender':'server',
                                'response':'error',
                                'content':'Username taken'}
                    self.send_data(response)
                else:
                    #login successfull
                    #add user in users
                    clients[self] = content
                    #Send history

                    response = {'timestamp':time.strftime("%H:%M:%S"),
                                'sender':'server',
                                'response':'info',
                                'content':"Login succesful"}
                    self.send_data(response)
                    response = {'timestamp':time.strftime("%H:%M:%S"),
                                'sender':'server',
                                'response':'history',
                                'content':'\n'.join(messages)}
                    self.send_data(response)
                    self.logged_in = True

            elif client_request == "logout":
                if self.logged_in:
                    del clients[self]
                    response = {'timestamp':time.strftime("%H:%M:%S"),
                                'sender':'server',
                                'response':'info',
                                'content':"Logout succesful"}
                    self.send_data(response)
                    self.logged_in = False
                else:
                    response = {'timestamp':time.strftime("%H:%M:%S"),
                                'sender':'server',
                                'response':'error',
                                'content':'Not logged in'}
                    self.send_data(response)

            elif client_request == "msg":
                if self.logged_in:

                    response = {'timestamp':time.strftime("%H:%M:%S"),
                                'sender':clients[self],
                                'response':'message',
                                'content':content}
                    messages += ["<"+ response.get('timestamp') + "> " +
                                 clients[self] + ": " + content]
                    for client in clients:
                        client.send_data(response)
                else:
                    response = {'timestamp':time.strftime("%H:%M:%S"),
                                'sender':'server',
                                'response':'error',
                                'content':'Not logged in'}
                    self.send_data(response)

            elif client_request == "names":
                if self.logged_in:
                    names = ""
                    for client in clients:
                        names += clients[client] + "\n"
                        response = {'timestamp':time.strftime("%H:%M:%S"),
                                    'sender':clients[self],
                                    'response':'info',
                                    'content':names}
                        self.send_data(response)
                else:
                    response = {'timestamp':time.strftime("%H:%M:%S"),
                                'sender':'server',
                                'response':'error',
                                'content':'Not logged in'}
                    self.send_data(response)

            elif client_request == "help":
                response = {'timestamp':time.strftime("%H:%M:%S"),
                            'sender':'server',
                            'response':'info',
                            'content':help_text}
                self.send_data(response)
            else:
                response = {'timestamp':time.strftime("%H:%M:%S"),
                            'sender':'server',
                            'response':'error',
                            'content':"Unknown command"}
                self.send_data(response)

    def send_data(self,data):
        self.request.sendall(json.dumps(data))

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """

    HOST, PORT = 'localhost', 9998
    print 'Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
