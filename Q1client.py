import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 12345)

client_socket.connect(server_address)



message = ("hello bhai kaise ho, sub thik thak h na  ")
client_socket.send(message.encode('utf-8'))



# Receive a response from the server
response = client_socket.recv(1024)
print(f"Server response: {response.decode('utf-8')}")



# Close the client socket
client_socket.close()
