import asyncio
from asyncio import sleep
from time import sleep as synch_sleep


async def waiter_1():

    for _ in range(3):
        print("Я ждун №1, и я жду...")
        await sleep(1)


async def waiter_2():

    for _ in range(3):
        print("Я ждун №2, и я жду...")
        await sleep(1)


async def waiter_3():

    for _ in range(3):
        print("Я ждун №3, и я жду...")
        await sleep(1)


async def main_async_function():
    # Когда мы обозначаем функцию как async, то мы по сути делаем из нее не обыкновенную функцию,
    # а нечто навроде генератора, только асинхронного. И она возвращает уже не результат выполнения функции,
    # а т.н. корутину (corutine).
    # Эти корутины мы помещаем в список, и всем скопом кидаем в event_loop, где они будут выполняться, передавая управление
    # друг другу в соответствии с тем, где у них внутри расположены await.
    # await по сути значит, что в этом месте мы останавливаем исполнение функции, чтобы ожидать выполнения других
    # _асинхронных_ (!) функций (тоже корутин). Когда эти корутины выполнятся, то event loop скажет интерпретатору об этом,
    # и выполнение продолжится.
    # tasks = [
    #     waiter_1(),
    #     waiter_2(),
    #     waiter_3(),
    # ]
    #
    # await asyncio.gather(*tasks)
    loop = asyncio.get_event_loop()
    loop.create_task(waiter_1())
    loop.create_task(waiter_2())
    loop.create_task(waiter_3())


if __name__ == "__main__":
    # event_loop = asyncio.get_event_loop()
    # event_loop.run_until_complete(main_async_function())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_async_function())
    loop.run_forever()
    print("Все?")
