#  Create a TCP server in Python that echoes back any message received from clients. Test the server using a Python client program. Explain the flow of data between the server and client.

import socket

server_host = '127.0.0.1' 
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_host, server_port))

server_socket.listen(10)
print(f"Server is listening on {server_host}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        client_socket.send(data)

    client_socket.close()
