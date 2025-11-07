import lazychatServer

chat = lazychatServer.LazyChat()

chat.connection("127.0.0.1", 5000)
chat.listen(listeningProtocol='lazy', bufferSize=5000)