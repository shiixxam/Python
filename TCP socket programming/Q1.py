# Writing Python scripts for implementing TCP client-server interactions.

#SERVER SIDE

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 12345)

server_socket.bind(server_address)

server_socket.listen(5)

print("Server is waiting for a connection...")

client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

data = client_socket.recv(1024)
print(f"Received from client: {data.decode('utf-8')}")

response = "Message received! Thank you."
client_socket.send(response.encode('utf-8'))

client_socket.close()
server_socket.close()
