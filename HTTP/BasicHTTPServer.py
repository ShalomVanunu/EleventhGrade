 #Python3.7+
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
HOST, PORT = local_ip, 80


listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen()
print(f'Serving HTTP on port {PORT} ...IP {local_ip}')
while True:
    client_connection, client_address = listen_socket.accept()
    print(client_address[0])
    request_data = client_connection.recv(1024)
    if "Android" in request_data.decode():
        http_response = b"""\
        HTTP/1.1 200 OK\n
        <h1>you surf from android</h1>
        """
        client_connection.sendall(http_response)
    #print(request_data.decode('utf-8'))
    else:
        http_response = b"""\
    HTTP/1.1 200 OK\n
    <h1>Hello, World!</h1>
    """
        client_connection.sendall(http_response)
    client_connection.close()
