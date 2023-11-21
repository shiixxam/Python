import asyncio

async def read_messages(reader):
    while True:
        data = await reader.read(100)
        if not data:
            break
        message = data.decode()
        print(f"Received from server: {message}")

async def send_messages(writer):
    while True:
        message = input("Enter a message (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        writer.write(message.encode())
        await writer.drain()

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    asyncio.create_task(read_messages(reader))
    await send_messages(writer)

    print("Closing the connection")
    writer.close()
    await writer.wait_closed()

asyncio.run(main())
