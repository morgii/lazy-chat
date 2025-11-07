import lazychat

chat = lazychat.LazyChat()

chat.connection("127.0.0.1", 5000)
chat.listen(1024)