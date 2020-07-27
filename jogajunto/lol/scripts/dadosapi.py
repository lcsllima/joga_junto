import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')


def header():

    headers = {
        "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": api_key
    }

    return headers
