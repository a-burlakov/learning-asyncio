import asyncio
from asyncio import sleep

QUERY = "INSERT INTO some_test_table VALUES ($1, $2, $3)"


async def make_request():
    await sleep(0.1)


async def main():
    chunk = 200
    tasks = []
    pended = 0
    for x in range(1000):
        task = asyncio.create_task(make_request())
        pended += 1
        tasks.append(task)

        if len(tasks) == 200 or pended == 10_000:

            res = await asyncio.gather(*tasks)
            tasks.clear()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
