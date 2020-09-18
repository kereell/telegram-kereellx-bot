#!/usr/bin/env python3
import requests
from logging import getLogger

logger = getLogger(__name__)

class BittrexRequestError(BittrexError):
    """Eror on wrong url
    """


class BittrexClient(object):

    def __init__(self):
        self.base_url = "https://api.bittrex.com/api/v1.1"

    def __request(self, method, params):
        url = self.base_url + method

        try:
            r = requests.get(url=url, params=params)
            result = r.json()
        except Exception:
            logger.exception("Bittrex error")
            raise BittrexError

        if result.get("success"):
            return result
        else:
            logger.error("Request error: %s", result.get("message"))
            raise BittrexRequestError
       
    def get_ticker(self, pair):
        params = {
            "market": pair
        }
        return self.__request(method="/public/getticker", params=params)
