# import socket

# server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# print('socket created')

# server_socket.bind(('localhost',9999))

# server_socket.listen(5)
# print('waiting for connections')

# while True:
#     client_socket, client_address = server_socket.accept()
#     print('connected with',client_address)
    

#     client_socket.send(bytes("hey client welcome to titwala","utf-8"))
#     client_socket.close()

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ("socket created successfully")

s.bind(('localhost',9999))
s.listen(10)
print("waiting for connection")

while True:
    c, address = s.accept()
    print('connected with',address)
    data = c.recv(1024)  

    if not data:
        break
    print("Received:", data.decode('utf-8'))
    
    c.send(bytes(" i am AI assist from Xresearch ","utf-8"))
    c.close()

