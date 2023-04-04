import asyncio
import threading
from asyncio import sleep
from contextvars import ContextVar

MyCounter = ContextVar("counter", default=0)


async def increase():
    my_counter = MyCounter.get()
    my_counter += 1
    MyCounter.set(my_counter)


async def count():
    while True:
        await increase()
        my_counter = MyCounter.get()
        print(f"Счетчик: {my_counter}")

        await sleep(1)


async def main():
    pass


if __name__ == "__main__":
    asyncio.run(count())
