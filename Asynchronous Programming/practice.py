# import asyncio

# async def  main ():
#     print("hello world")
#     await asyncio.sleep(2)
#     print("kaise ho aap sab")

# asyncio.run(main())




# async def shivam():
#     print("shivam")
#     await asyncio.sleep(2)
# async def harsh():
#     print("harsh")
#     await asyncio.sleep(2)
# async def kiran():
#     print("kiran")
#     await asyncio.sleep(2)

# asyncio.run(shivam())
# asyncio.run(harsh())
# asyncio.run(kiran())


# async def main():
#     await asyncio.gather(shivam(),harsh(),kiran())

# asyncio.run(main())




# import asyncio

# async def task1():
#     print("task 1 has started")
#     await asyncio.sleep(2)
#     print ("task 1 completed")

# async def task2():
#     print("task2 has started")
#     await asyncio.sleep(2)
#     print("task 2 is completed")

# async def main():
#     print("main program has started ")

#     task_1=asyncio.create_task(task1())
#     task_2=asyncio.create_task(task2())

#     await task_1
#     await task_2

#     print("main program has completed")

# asyncio.run(main())





# import asyncio


# async def shivam():
#     print("server 1 is started")
#     await asyncio.sleep(2)
#     print("server 1 is stopped")

# async def harsh():
#     print("server 2 is started")
#     await asyncio.sleep(4)
#     print("server 2 is stopped")

# async def main():
#     task1= asyncio.gather(shivam(),harsh())
#     await task1
# asyncio.loop.run_until_complete(main())

# # asyncio.run(shivam())
# # asyncio.run(harsh())


import asyncio

async def shivam():
    print("server 1 is started")
    await asyncio.sleep(4.2)
    print("server 1 is stopped")

async def harsh():
    print("server 2 is started")
    await asyncio.sleep(4.3)
    print("server 2 is stopped")

async def main():
    task1 = asyncio.create_task(shivam())
    task2 = asyncio.create_task(harsh())
    
    await asyncio.gather(task1, task2)

loop = asyncio.get_event_loop()

loop.run_until_complete(main())

loop.close()
