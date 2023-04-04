import asyncio
from time import sleep


def make_request(cnt):
    print("Запрос к БД:", cnt)
    sleep(0.1)


if __name__ == "__main__":

    cnt = 0
    for _ in range(100):
        make_request(cnt)
        cnt += 1
