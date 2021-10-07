import socket
import threading
import time

MSG_LENGHT = 2048
PORT = 1234
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "172.20.155.214"
ADDR = (SERVER, PORT)

# Choosing Nickname
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Listening to Server and Sending Nickname
def receive(client):
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(MSG_LENGHT).decode(FORMAT)
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Sending Messages To Server
def write(client):
    while True:
        message = input()
        message = '['+nickname+'] :'+message
        client.send(message.encode(FORMAT))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive, args=(client,))
receive_thread.start()


write_thread = threading.Thread(target=write, args=(client,))
write_thread.start()




