#Asynchronous file I/O and database operation

import asyncio
import aiofiles

async def read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        content = await file.read()
        print(f"Read from {file_path}: {content}")

async def write_file(file_path, content):
    async with aiofiles.open(file_path, mode='w') as file:
        await file.write(content)
        print(f"Wrote to {file_path}")

async def main():
    file_path = 'example.txt'
    content_to_write = 'Hello, Async I/O!'

    await write_file(file_path, content_to_write)

    await read_file(file_path)

# Run the asynchronous event loop
asyncio.run(main())

