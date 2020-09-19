#!/usr/bin/env python3
from logging import getLogger
from bittrex import BittrexClient
from bittrex import BittrexError
import os

notify_pair = os.environ["TG_TOKEN"]
logger = getLogger(__name__)


def main():
    client = BittrexClient()
    try:
        current_price = client.get_last_price(pair=notify_pair)
        message = "{} = {}".format(notify_pair, current_price)
    except BittrexError:
        logger.error("BittrexError")
        message = "An error happend"

    print(message)


if __name__ == '__main__':
    main()
