# import asyncio



# import asyncio

# async def handle_client(reader,writer):
#     data = await reader.read(100)
#     message = data.decode()
#     addr= writer.get_extra_info("peername")

#     print(f"received {message} from {addr}")

#     print("send : {r}.format(message)")

# import asyncio

# async def handle_client(reader, writer):
#     data = await reader.read(100)
#     message = data.decode()
#     addr = writer.get_extra_info('peername')

#     print(f"Received {message!r} from {addr}")

#     print("Send: {!r}".format(message))
#     writer.write(data)
#     await writer.drain()

#     print("Closing the connection")
#     writer.close()

# async def main():
#     server = await asyncio.start_server(
#         handle_client, '127.0.0.1', 8888)

#     addr = server.sockets[0].getsockname()
#     print(f'Serving on {addr}')

#     async with server:
#         await server.serve_forever()

# asyncio.run(main())


# import asyncio
# import websockets
# import json
# import uuid
# import datetime

# authenticated_users = {}
# connected_users = {}

# async def handle_client(websocket, path):
#     user_id = uuid.uuid4()
#     connected_users[user_id] = websocket

#     while True:
#         try:
#             message = await websocket.recv()
#             message_data = json.loads(message)

#             if message_data["type"] == "message":
#                 recipient_id = message_data["recipient_id"]

#                 if recipient_id in connected_users:
#                     recipient_socket = connected_users[recipient_id]

#                     message_data["sender_id"] = user_id
#                     message_data["sender_name"] = authenticated_users[user_id]
#                     message_data["timestamp"] = str(datetime.datetime.now())

#                     message_json = json.dumps(message_data)
#                     await recipient_socket.send(message_json)
#                 else:
#                     error_message = {"type": "error", "message": "Invalid recipient ID"}
#                     message_json = json.dumps(error_message)
#                     await websocket.send(message_json)

#             elif message_data["type"] == "authentication":
#                 username = message_data["username"]
#                 authenticated_users[user_id] = username

#                 message_data["type"] = "authentication_success"
#                 message_json = json.dumps(message_data)
#                 await websocket.send(message_json)

#         except Exception as e:
#             print(f"Error handling message from user {user_id}: {e}")

# async def handle_client_disconnect(websocket, path):
#     user_id = list(connected_users.keys())[list(connected_users.values()).index(websocket)]

#     del connected_users[user_id]
#     del authenticated_users[user_id]

#     print(f"User {user_id} disconnected.")

# start_server = websockets.serve(handle_client, "localhost", 8000)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
# import asyncio

# async def handle_client(reader, writer):
#     while True:
#         data = await reader.read(100)
#         if not data:
#             break

#         message = data.decode()
#         addr = writer.get_extra_info('peername')
#         print(f"Received {message} from {addr}")

#         response = f"Server received: {message}"
#         writer.write(response.encode())
#         await writer.drain()

#     print("Closing the connection")
#     writer.close()

# async def main():
#     server = await asyncio.start_server(
#         handle_client, '127.0.0.1', 8888)

#     addr = server.sockets[0].getsockname()
#     print(f'Serving on {addr}')

#     async with server:
#         await server.serve_forever()

# # Run the server
# asyncio.run(main())


import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Client connected: {addr}")

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break

            message = data.decode()
            print(f"Received from {addr}: {message}")

            response = f"Server received: {message}"
            writer.write(response.encode())
            await writer.drain()

    except asyncio.CancelledError:
        pass

    finally:
        print(f"Client disconnected: {addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
