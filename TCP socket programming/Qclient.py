import socket

server_host = '127.0.0.1'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_host, server_port))

while True:
    message = input("Enter a message (or type 'exit' to quit): ")
    if message == 'exit':
        break

    client_socket.send(message.encode('utf-8'))

    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode('utf-8')}")

client_socket.close()
