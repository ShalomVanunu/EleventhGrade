import socket


PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.1.220"
ADDR = (SERVER, PORT)

print("[STARTING] Clinet is starting...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.send("shalom".encode(FORMAT))
client.close()





