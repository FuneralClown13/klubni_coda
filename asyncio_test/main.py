import asyncio
from asyncio import run, create_task
from aiohttp import ClientSession


async def get_():
    url = 'https://api.adviceslip.com/advice'
    async with ClientSession() as session:
        async with session.get(url) as response:
            await asyncio.sleep(5)
            print(await response.text())




async def main(num):
    tasks = []
    for _ in range(num):
        tasks.append(create_task(get_()))
    for task in tasks:
        await task

if __name__ == '__main__':
    run(main(5))
