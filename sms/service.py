import re
import requests
from environs import Env

env = Env()
env.read_env()


def send(phone: int, text: str):
        url: str = env.str('url')
        login: str = env.str('login')
        pwd: str = env.str('pwd')
        headers = {'content-type': 'application/json'}
        data = {
                "login": login,
                "pwd": pwd,
                "CgPN": "AgroZamin",
                "CdPN": phone,
                "text": text
        }
        response = requests.post(url=url, headers=headers, json=data)
        return response.status_code


def multiple_replace(text, word_dict):
        pattern = re.compile("|".join(map(re.escape, word_dict.keys())))
        return pattern.sub(lambda x: word_dict[x.group(0)], text)