#!/usr/bin/env python3
import requests
from logging import getLogger

logger = getLogger(__name__)

class BittrexError(Exception):
    """Error: Unknow error during API Bittrex request
    """

class BittrexRequestError(BittrexError):
    """Eror: Wrong request
    """

class BittrexClient(object):

    def __init__(self):
        self.base_url = "https://api.bittrex.com/api/v1.1"

    def __request(self, method, params=None) -> dict:
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
       
    def get_ticker(self, pair) -> dict:
        params = {
            "market": pair
        }
        return self.__request(method="/public/getticker", params=params)


    def get_last_price(self, pair) -> float:
        res = self.get_ticker(pair=pair)
        return res["result"]["Last"]
        

    def get_markets(self) -> dict:
        return self.__request(method="/public/getmarkets")


    def get_all_names(self):
        res = self.get_markets()
        for cur in res['result']:
            if cur['BaseCurrency'] == 'USD':
                yield cur['MarketCurrency']


    def get_market_summaries(self) -> dict:
        return self.__request(method="/public/getmarketsummaries")


    def get_last_prices(self, pairs: list):
        for i in res['result']:
            if i['MarketName'] in pairs:
                yield i ['MarketName'], i['last']
