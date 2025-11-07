import socket
class LazyChatClient():
    def __init__(self):
        print("LazyChatClient started")

    #ip: server ip where client will connect
    #type : string
    #port: port of server
    #type : int
    def clientConnection(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 and TCP connection
        self.sock.connect((ip,port))

    #param sendProtocol :  Type of protocol that client will understand and use
    #type : string
    #data : data to send
    #type : string
    def send(self, sendProtocol, data):
        self.sendProtocol = sendProtocol
        self.data = data

        if sendProtocol == 'lazy':
            self.sock.sendall(data.encode())