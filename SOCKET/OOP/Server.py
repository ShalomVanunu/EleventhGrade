

import socket

class Server:

    def __init__(self, host, port):
        self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def bind(self):
        self.serverSocket.bind((self.host, self.port))
        self.serverSocket.listen()

    def run(self):
        while True:
            print ('Waiting for a connection')
            (clientSocket, addr) = self.serverSocket.accept()
            print ('Got a connection from {}'.format(str(addr)))
            message = 'Congrats! You have connected'
            self.sendMessage(message, clientSocket)
            self.recieveMessage(clientSocket)
            clientSocket.close()

    def sendMessage(self, message, clientSocket):
        clientSocket.send(message.encode('ascii'))

    def recieveMessage(self,clientSocket):
        message = clientSocket.recv(1024).decode('ascii')
        print(message)

    def closeSocket(self):
        self.serverSocket.close()


if __name__ == '__main__':
    myServer = Server('0.0.0.0', 5555)
    myServer.bind()
    myServer.run()
 #   myServer.recieveMessage()
    myServer.closeSocket()