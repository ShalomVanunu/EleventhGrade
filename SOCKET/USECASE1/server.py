import socket 

MSG_LENGHT = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print("[STARTING] server is starting...")
server.listen()
print(f"[LISTENING] Server is listening on {SERVER}")
conn, addr = server.accept()
print(f"[NEW CONNECTION] {addr} connected.")

msg = conn.recv(MSG_LENGHT).decode(FORMAT)
print(msg)

conn.close()






