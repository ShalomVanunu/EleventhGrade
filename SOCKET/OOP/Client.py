
import socket


class Client:

    def __init__(self, host, port):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def connect(self):
        self.serverSocket.connect((self.host, self.port))

    def getMessage(self):
        return self.serverSocket.recv(1024).decode('ascii')

    def modifyMessage(self):
        return message.upper()

    def sendMessage(self, upperCaseMessage):
        self.serverSocket.send(upperCaseMessage.encode('ascii'))

    def closeConnection(self):
        self.serverSocket.close()


if __name__ == '__main__':
    myClient = Client('192.168.1.242', 5555)
    myClient.connect()
    message = myClient.getMessage()
    upperCaseMessage = myClient.modifyMessage()
    print(upperCaseMessage)
    myClient.sendMessage(upperCaseMessage)
    myClient.closeConnection()