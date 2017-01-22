import socket

class TCPConnection:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        try:
            self.sock.connect((host, port))
            print('Successful Connection')
        except:
            print('Connection Failed')

    def readlines(self):
        data = self.sock.recv(1024)
        print(data)



listen = TCPConnection()
listen.connect('localhost',7000)
listen.readlines()