import asyncio

clients = []

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Client connected: {addr}")

    clients.append(writer)

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break

            message = data.decode()
            print(f"Received from {addr}: {message}")

            # Broadcast the message to all clients
            await broadcast(message, writer)

    except asyncio.CancelledError:
        pass

    finally:
        print(f"Client disconnected: {addr}")
        # Remove the client from the list
        clients.remove(writer)
        writer.close()
        await writer.wait_closed()

async def broadcast(message, sender):
    # Send the message to all clients except the sender
    for client in clients:
        if client != sender:
            try:
                client.write(message.encode())
                await client.drain()
            except:
                # Handle exceptions (e.g., if a client connection is lost)
                pass

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

# Run the server
asyncio.run(main())
