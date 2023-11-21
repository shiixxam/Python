# import asyncio

# async def send_message(message):
#     reader, writer = await asyncio.open_connection(
#         '127.0.0.1', 8888)

#     print(f"Send: {message!r}")
#     writer.write(message.encode())
#     await writer.drain()

#     data = await reader.read(100)
#     print(f"Received: {data.decode()!r}")

#     print("Closing the connection")
#     writer.close()

# asyncio.run(send_message('Hello, server!'))

# import websocket
# import asyncio
# import autobahn as wab
# import json
# import uuid

# async def authenticate(username):
#     async with wab.connect("ws://localhost:8000") as connection:
#         print("Connecting to chat server for authentication...")

#         message_data = {
#             "type": "authentication",
#             "username": username
#         }

#         message_json = json.dumps(message_data)
#         await connection.send(message_json)

#         response = await connection.recv()
#         response_data = json.loads(response)

#         if response_data["type"] == "authentication_success":
#             print("Authentication successful. You are now connected as", username)
#             return connection
#         else:
#             print("Authentication failed. Please try again.")
#             return None

# async def connect(username):
#     connection = await authenticate(username)

#     if connection:
#         print("Connected to chat server.")

#         while True:
#             message = await input("Enter message: ")
#             message_data = {
#                 "type": "message",
#                 "recipient_id": "user2",
#                 "sender_id": uuid.uuid4(),
#                 "sender_name": username,
#                 "message": message
#             }

#             message_json = json.dumps(message_data)
#             await connection.send(message_json)

#     else:
#         print("Unable to connect to chat server.")

# async def main():
#     username = input("Enter your username: ")
#     await connect(username)

# asyncio.run(main())
# asyncio.run(connect())


# import asyncio

# async def tcp_client(message):
#     reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

#     print(f"Send: {message!r}")
#     writer.write(message.encode())

#     data = await reader.read(100)
#     print(f"Received: {data.decode()!r}")

#     print("Closing the connection")
#     writer.close()

# # Run the client
# asyncio.run(tcp_client('Hello, server!'))

