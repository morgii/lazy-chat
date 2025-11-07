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
    def connection(self, ip: str, port: int):         #establish lazychat connection
        self.ip = ip
        self.port = port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 and TCP connection
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((ip,port))
            self.sock.listen(5)
            print(f"Connected with {ip}:{port} - LazyChat listening")
        except OSError as e:
            print(f"[Error] Failed to bind or listen on {ip}:{port} → {e}")
        except Exception as e:
            print(f"[Unexpected Error] During connection setup: {e}")


    #:param listeningProtocol: Type of protocol that server will understand
    #type : string
    #:param bufferSize: The content wich the server will recieve
    #:type : int
    def listen(self, listeningProtocol: str ,bufferSize: int):
        self.listeningProtocol = listeningProtocol
        self.bufferSize = bufferSize
        try:
            conn, addr = self.sock.accept()
            print(f"Client connected from {addr}")
        except Exception as e:
            print(f"[Error] Accepting connection failed: {e}")
            return

        while True:
            try:
                data = conn.recv(bufferSize)
                if not data:
                    print("Client disconnected.")
                    break

                if listeningProtocol == 'http':
                    try:
                        method, path, headers, body = parsehttp.parse_http_request(data)
                        print(method, path, headers, body)
                    except Exception as e:
                        print(f"[HTTP Parse Error] {e}")

                elif listeningProtocol == 'lazy':
                    try:
                        method, auth, json = parselazy.parse_lazy_request(data)
                        print(f'''
                        "method": {method}, 
                        "auth": {auth}, 
                        "json": {json}''')
                    except Exception as e:
                        print(f"[Lazy Parse Error] {e}")

                else:
                    print(f"[Warning] Unknown protocol: {listeningProtocol}")

            except ConnectionResetError:
                print("Connection reset by client.")
                break
            except Exception as e:
                print(f"[Error] While receiving data: {e}")
                break

        conn.close()
        print("Connection closed.")
