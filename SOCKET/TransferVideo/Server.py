
import socket

PORT =8888
IP = '0.0.0.0'

my_server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_server.bind((IP,PORT))

my_server.listen()

client_obj, client_addr_port = my_server.accept()


data_recv = client_obj.recv(1200000)


file = open('bech_rcv.mp4','wb')
file.write(data_recv)

msg_send = 'file recived'
client_obj.send(msg_send.encode())

my_server.close()

