import asyncio
import threading
from asyncio import sleep


def multiply(a, b):
    return a * b


def generator(a, b):
    while True:
        yield a * b
        a = a + 1


async def async_function(a):
    while True:
        await a
        a = a + 1


if __name__ == "__main__":
    a = async_function(2)
    print(dir(a))
