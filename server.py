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