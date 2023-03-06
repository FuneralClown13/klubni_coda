import requests
from dotenv import load_dotenv
import os

load_dotenv()
IAM_TOKEN = os.getenv('IAM_TOKEN')
folder_id = os.getenv('folder_id')
target_language = 'ru'


def translate(texts: list[str]):
    if not texts:
        return 'Empty text'

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )
    resp_json = response.json()
    return [resp_json['translations'][i]['text'] for i in range(len(texts))]

if __name__ == '__main__':
    print(translate(['Hello', 'world']))
