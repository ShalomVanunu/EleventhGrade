
import  socket
import threading

FORMAT = "utf-8"

class Server:

    def __init__(self, host, port):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.socket_list =[]
        self.address_list = []

    def bind(self):
        self.serverSocket.bind((self.host,self.port))

    def handleSockets(self):
        while True:
            self.recieveMessage()
            message =  "Msg Received "
            self.sendMessage(message)

    def run(self):
        self.serverSocket.listen()
        while True:
            print("Waiting for Clients Connection.....")
            self.clientSocket, self.addr  = self.serverSocket.accept()
            self.socket_list.append(self.clientSocket)
            self.address_list.append(self.addr[0])
            print(f'Active Connections {threading.active_count()} Got Connection from {self.address_list}')
            message = "Welcome ! you are connected"
            self.sendMessage(message)
            thread = threading.Thread(target=self.handleSockets)
            thread.start()

    def sendMessage(self,message):
        self.clientSocket.send(message.encode(FORMAT))

    def recieveMessage(self):
        message = self.clientSocket.recv(1024).decode(FORMAT)
        print(message)

if __name__ == '__main__':
    myServer = Server('172.20.155.215', 6565)
    myServer.bind()
    myServer.run()