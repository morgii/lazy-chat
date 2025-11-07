import socket
import parsehttp
import parselazy

class LazyChat:
    def __init__(self):
        print("LazyChat activated")
    
    #:param ip: The IP address which server will listen.
    #:type : string
    #:param port: The port number on which the server will listen.
    #:type port: int
    def connection(self, ip, port):         #establish lazychat connection
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 and TCP connection
        self.sock.bind((ip,port))
        self.sock.listen(5)
        print(f"Connected with {ip}:{port} - LazyChat listening")


    #:param listeningProtocol: Type of protocol that server will understand
    #type : string
    #:param bufferSize: The content wich the server will recieve
    #:type : int
    def listen(self, listeningProtocol,bufferSize):
        self.listeningProtocol = listeningProtocol
        self.bufferSize = bufferSize
        conn, addr = self.sock.accept()
        while True:
            print(f"Connected with {addr}")
            data = conn.recv(bufferSize)

            if listeningProtocol == 'http':
                method, path, headers, body = parsehttp.parse_http_request(data)
                print(method, path, headers, body)

            elif listeningProtocol == 'lazy':
                value = parselazy.parse_lazy_request(data)
                print(value)






