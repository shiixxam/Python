
#  Develop a Python UDP server that accepts messages from clients and displays them. Test the server using multiple Python clients. Discuss any challenges faced during UDP communication

import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("UDP server is listening on {}:{}".format(*server_address))

try:
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received message from {client_address}: {data.decode('utf-8')}")

except OSError as e:
    print(f"Socket error: {e}")
finally:
    server_socket.close()
