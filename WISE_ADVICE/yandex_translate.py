import asyncio
import time
from aiohttp import ClientSession
import requests
from dotenv import load_dotenv
import os
from get_IAM_TOKEN import get_IAM_TOKEN

load_dotenv()
IAM_TOKEN = os.getenv('IAM_TOKEN')
folder_id = os.getenv('folder_id')
target_language = 'ru'

start_time = time.time()


async def get_translate(text: str):
    body = {
        "targetLanguageCode": target_language,
        "texts": text,
        "folderId": folder_id,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }
    async with ClientSession() as session:
        async with session.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                json=body,
                                headers=headers) as resp:
            advice_json = await resp.json()
            return advice_json['translations'][0]['text']


async def start_translate(text_list):
    tasks = []
    ru_text = []
    for text in text_list:
        tasks.append(asyncio.create_task(get_translate(text)))
    for task in tasks:
        ru_text.append(await task)

    return ru_text


def translate(text):
    global start_time
    if (time.time() - start_time) > 86400:
        start_time = time.time()
        get_IAM_TOKEN()
    return asyncio.run(start_translate(text))


if __name__ == '__main__':
    start = time.time()
    ex = ['Life is better when you sing about bananas.',
          'Identify sources of happiness.',
          "Don't let the bastards grind you down.",
          'Do, or do not. There is no try.',
          'If you think your headphones are dying, check the socket for fluff with a straightened paperclip.']

    print(asyncio.run(start_translate(ex)))
    print(time.time() - start)
