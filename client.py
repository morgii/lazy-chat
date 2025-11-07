import lazychatClient

serverIp = "127.0.0.1"
serverPort = 5000


chat = lazychatClient.LazyChatClient()

chat.clientConnection(serverIp, serverPort)
while True:
    chat_data = input("Send msg: ")
    chat.send(sendProtocol='lazy', data=chat_data)