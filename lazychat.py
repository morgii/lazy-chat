import socket
import parsehttp

class LazyChat:
    def __init__(self):
        print("LazyChat activated")

    def connection(self, ip, port):         #establish lazychat connection
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 and TCP connection
        self.sock.bind((ip,port))
        self.sock.listen(5)
        print(f"Connected with {ip}:{port} - LazyChat listening")

    def listen(self, bufferSize):
        self.bufferSize = bufferSize
        while True:
            conn, addr = self.sock.accept()
            print(f"Connected with {addr}")
            data = conn.recv(bufferSize)
            #print(data)
            method, path, headers, body = parsehttp.parse_http_request(data)
            print(method, path, headers, body)



