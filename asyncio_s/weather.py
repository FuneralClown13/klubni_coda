import asyncio, aiohttp
import json
import requests
from functools import lru_cache
from get_cities_list import get_cities_list, set_city_in_list, del_city_if_404
import time
import re

cities = '@'.join(get_cities_list())


async def get_city_weather(city):
    global cities
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            print(resp.status)
            if resp.status == 404 and city in cities:
                del_city_if_404(city)
                 cities = '@'.join(get_cities_list())
                return ''
            if resp.status == 200 and city not in cities:
                set_city_in_list(city)
            weather_json = await resp.json()
            temp = (weather_json["main"]["temp"] - 273.15)
            return f'{city}: {weather_json["weather"][0]["main"]} {temp:.1f}°C'


async def city_list(city_key):
    cities_list = re.findall(fr'{city_key}+[a-z]*', cities)[:5]
    print(cities_list)
    if not cities_list:
        return [city_key]
    return cities_list


async def start_get_weather(city_key):
    task = asyncio.create_task(city_list(city_key))
    cities_to_task = []
    cities_to_task += await task

    city_weather = []
    tasks = []
    for city in cities_to_task:
        tasks.append(asyncio.create_task(get_city_weather(city)))

    for task in tasks:
        city_weather.append(await task)
    print(city_weather)
    return city_weather


def weather(city_key):
    return asyncio.run(start_get_weather(city_key))


if __name__ == '__main__':
    start = time.time()
    asyncio.run(start_get_weather('Kali'))
    print(time.time() - start)
