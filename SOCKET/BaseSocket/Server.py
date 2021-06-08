import socket

SERVERIP = "172.20.145.216" #The IP of Server
PORT = 5050 # well known PORTs  (1-1023)

#Phase 1 - Create socket Object
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #socket.AF_INET = IPv4   || SOCK_STREAM -TCP SOCK_DGRAM-UDP

# Phase 2 - Bind the Object to MY IP,and PORT
server.bind((SERVERIP,PORT))  #Tupple

print(" The Server is UP")

# Phase 3 - getiing the Server to Listen
server.listen()

# Phase 4 - wait for Client to connect and get his adress and Conn Obect
conn, address = server.accept()

print(f" The Client {address} is connected")

#Phase 5 - get the data from client. no more than 500 bytes. decode the data in utf-8
msg = conn.recv(500).decode('utf-8')

print(msg)

#Phase 6 - Close the Connection
conn.close()
