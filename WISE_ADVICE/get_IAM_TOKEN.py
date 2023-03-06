import os
import subprocess
import json
import dotenv


def get_IAM_TOKEN():
    dotenv.load_dotenv()
    OAuth_token = os.getenv('OAuth_token')

    IAM_TOKEN = subprocess.run(['curl',
                                '-d',
                                '{\"yandexPassportOauthToken\":\"' + OAuth_token + '\"}',
                                'https://iam.api.cloud.yandex.net/iam/v1/tokens'],
                               stdout=subprocess.PIPE,
                               text=True)
    IAM_TOKEN = json.loads(IAM_TOKEN.stdout)['iamToken']
    os.putenv('IAM_TOKEN', IAM_TOKEN)

    with open('.env', 'r+') as env:
        env.write(f'IAM_TOKEN = "{IAM_TOKEN}"')
