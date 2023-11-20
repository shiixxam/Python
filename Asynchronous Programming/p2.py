import asyncio

async def foo():
    print("Foo")

async def bar():
    print("Bar")

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(foo(), bar()))
