import asyncio

async def send_message(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f"Send: {message!r}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"Received: {data.decode()!r}")

    print("Closing the connection")
    writer.close()

asyncio.run(send_message('Hello, server!'))
