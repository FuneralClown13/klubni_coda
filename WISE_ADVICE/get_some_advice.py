import time
from asyncio import run, create_task
from aiohttp import ClientSession
import json


async def __get_some_advice():
    url = 'https://api.adviceslip.com/advice'
    async with ClientSession() as session:
        async with session.get(url) as response:
            advice = json.loads(await response.text())
            return advice['slip']['advice'], advice['slip']['id']


async def __tasks_builder(amount_advice: int) -> list[str]:
    tasks = []
    advice = []
    for _ in range(amount_advice):
        tasks.append(create_task(__get_some_advice()))
    for task in tasks:
        advice.append(await task)
    return advice


def main_get_advice(amount_advice: int):
    return run(__tasks_builder(amount_advice))


if __name__ == '__main__':
    start = time.time()
    print(main_get_advice(5))
    print(time.time() - start)
