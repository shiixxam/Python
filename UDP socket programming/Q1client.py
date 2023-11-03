import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)

while True:
    message = input("Enter a message: ")
    client_socket.sendto(message.encode('utf-8'), server_address)

    client_socket.close()
