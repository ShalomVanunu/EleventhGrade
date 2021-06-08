import socket

PORT = 5050
IPSERVER = "172.20.145.216"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((IPSERVER,PORT))

client.send("Hello Server".encode('utf-8'))

client.close()


