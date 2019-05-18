import requests
from django.core.exceptions import ObjectDoesNotExist

from choco_reddit.settings import REDDIT_BASE_URL

FEEDS = ('best', 'hot', 'new', 'random', 'rising', 'controversial')


class RedditClient(object):
    def __init__(self, access_token: str = None):
        self.access_token = access_token

    def _data_from(self, url: str, method: str = 'GET', data=None):
        data = {} if data is None else data
        headers = {
            'Authorization': f'bearer {self.access_token}',
            'User-Agent': 'My User Agent 1.0'
        }
        response = requests.request(
            method=method, url=f'{REDDIT_BASE_URL}{url}', headers=headers, data=data
        )
        # TODO: add exception handling by docs
        response.raise_for_status()
        return response.json()

    @property
    def user_info(self):
        data = self._data_from(url='api/v1/me')
        return {
            'name': data['name'],
            'avatar': data['icon_img']
        }

    def feed(self, feed_type: str):
        feed_type = 'best' if feed_type is None or feed_type == '' else feed_type
        if feed_type not in FEEDS:
            raise ObjectDoesNotExist
        return self._data_from(url=feed_type)['data']['children']

    def act(self, **kwargs):
        return self._data_from(url=f'api/{kwargs.pop("action")}', method='POST', data=kwargs)
