import asyncio
import threading
from asyncio import sleep


async def count(counter):
    print("Количество записей в списке:", len(counter))

    while True:
        await sleep(0.001)
        counter.append(1)


async def print_every_one_sec(counter):
    while True:
        await sleep(1)
        print("- 1 секунда прошла, количество записей: ", len(counter))


async def print_every_five_sec(counter):
    while True:
        await sleep(5)
        print("---- 5 секунд прошла, количество записей: ", len(counter))


async def print_every_ten_sec(counter):
    while True:
        await sleep(10)
        print("-------- 10 секунд прошла, количество записей: ", len(counter))


async def main():
    counter = list()

    tasks = [
        count(counter),
        print_every_one_sec(counter),
        print_every_five_sec(counter),
        print_every_ten_sec(counter),
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
