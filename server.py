import threading
import socket
import argparse
import os


class Server(threading.Thread):

    """
        How we manage server connections.

        Connections = a list of serversocket objects representing current active connections
        host = ip address of listening socket
        port = port number of listening socket

    """
    def __init__(self,host,port):
        super().__init__()
        self.connections = []
        self.host = host
        self.port = port

    def run(self):
        """
        Creates the listening socket. Utilize SO_REUSEADDR option to allow binding to a previously used socket address instead of assinging new port.
        ServerSocket objects are stored in the connections attribute
        """

  ##AF_INET is used to represent the address (and protocol) families. It is used as the first argument to socket. SOCK_STREAM is the default socket type 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host,self.port))

        sock.listen(1)
        print('Listening at', sock.getsockname())

        while True:
            sc, sockname = sock.accept()
            print('Accepted a new connection from {} to {}'.format(sc.getpeername(), sc.getsockname()))

            server_socket = ServerSocket(sc,sockname,self)

            server_socket.start()
            self.connections.append(server_socket)
            print('Ready to receive messages from: ', sc.getpeername())

            #create a broadcast function and remove connection(?)


class ServerSocket(threading.Thread):
    """
    Supports communications with a connected client.
        sc (socket.socket) = The connected socket.
        sockname (tuple) = The client socket address.
        server (Server) = The parent thread.
    """
    def __init__(self, sc, sockname, server):
        super().__init__()
        self.sc = sc
        self.sockname = sockname
        self.server = server

        #create a run function, send(?) and exit(?)