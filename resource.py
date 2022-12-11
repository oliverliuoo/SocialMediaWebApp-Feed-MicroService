import logging
from typing import List, Dict

import requests

import config


class Post:

    def __init__(self):
        pass

    @staticmethod
    def get_posts_by_user_ids_within_window(user_ids: List[str],
                                            window: int) -> List[Dict]:
        path = config.post_service_host + '/post/users'
        url = '{}?user_list={}&window={}'.format(path, ','.join(user_ids), window)
        try:
            rsp = requests.get(url)
            if rsp.status_code == 200:
                return rsp.json()['data']
            else:
                logging.warning('Failed to make post api call. error msg: {}'.format(rsp.text))
                return []
        except Exception as e:
            logging.error(e)
            return []


class User:

    def __init__(self):
        pass

    @staticmethod
    def get_user_followings(user_id: str) -> List[str]:
        url = config.user_service_host + '/followings/{}'.format(user_id)
        try:
            rsp = requests.get(url)
            if rsp.status_code == 200:
                return [record['Followings'] for record in rsp.json()]
            else:
                logging.warning('Failed to make post api call. error msg: {}'.format(rsp.text))
                return []
        except Exception as e:
            logging.error(e)
            return []
