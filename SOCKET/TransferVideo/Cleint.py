import socket

PORT =8888
IP = '192.168.1.231'

my_client  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_client.connect((IP,PORT))

file = open('MP4 Py.mp4','rb')
data_file = file.read()

my_client.send(data_file)

print(my_client.recv(1024).decode())

my_client.close()