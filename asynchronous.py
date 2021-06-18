# Reference

#     https://docs.python.org/ko/3/library/asyncio-task.html


import asyncio
import time


async def say_after(delay, words):
    await asyncio.sleep(delay)
    print(words)


async def main():
    print(f"started at {time.strftime('%X')}")  # formatted string

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

    task1 = asyncio.create_task(
        say_after(1, 'hi'))

    task2 = asyncio.create_task(
        say_after(2, 'bye'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# started at 00:16:27
# hello
# world
# finished at 00:16:30
# started at 00:16:30
# hi
# bye
# finished at 00:16:32
