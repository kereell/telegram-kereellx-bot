#!/usr/bin/env python3
from bittrex import BittrexClient
from bittrex import BittrexRequestError
import config

NOTIFY_PAIR = "USD-BTC"
NOTIFY_USER_ID = ''


def main():
    client = BittrexClient()
    try:
        current_price = client.get_last_price(pair=NOTIFY_PAIR)
        message= "{} = {}".format(NOTIFY_PAIR, current_price)
    except BittrexError:
        logger.error("BittrexError")
        message = "An error happend"

    bot = Bot(
        token=config.TELEGRAM_KEREELLXBOT_TOKEN
    )
    
    

    print("{}".format(current_price))


if __name__ == '__main__':
    main()
