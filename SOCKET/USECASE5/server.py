"""
https://www.neuralnine.com/tcp-chat-in-python/
"""

import socket
import threading

MSG_LENGHT = 2048
PORT = 1234
SERVER = '172.20.155.214'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()


# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message.encode(FORMAT))


# Handling Messages From Clients
def handle(client,nickname):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(MSG_LENGHT).decode(FORMAT)
            if DISCONNECT_MESSAGE in message:
                broadcast(f'{nickname} left!')
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left!')
            nicknames.remove(nickname)
            break


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname

        client.send('NICK'.encode(FORMAT))
        nickname = client.recv(MSG_LENGHT).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast(f"{nickname} joined!\n")
        client.send('Connected to server!'.encode(FORMAT))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,nickname))
        thread.start()

print('Server is on......')
receive()

