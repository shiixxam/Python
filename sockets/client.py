import socket

client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(("localhost",9999))

message = (" how r uhhhhhh..............")
client_socket.send(message.encode("utf-8"))

print(client_socket.recv(1024).decode())


