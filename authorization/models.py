import requests
from requests.auth import HTTPBasicAuth

from choco_reddit.settings import (
    REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET,
    REDDIT_REDIRECT_URL)


def access_token_from(code: str) -> str:
    url = 'https://www.reddit.com/api/v1/access_token'
    authorization = HTTPBasicAuth(
        username=REDDIT_CLIENT_ID, password=REDDIT_CLIENT_SECRET
    )
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDDIT_REDIRECT_URL
    }
    response = requests.post(
        url=url, headers=headers, data=data, auth=authorization
    )
    response.raise_for_status()
    return response.json()['access_token']
