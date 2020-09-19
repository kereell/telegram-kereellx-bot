#!/usr/bin/env python3
import os
import logging
from subprocess import Popen
from subprocess import PIPE
# import config
# from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from bittrex import BittrexClient
from bittrex import BittrexError
from bittrex import BittrexRequestError

KEREELLXBOT_TOKEN=os.environ["TG_TOKEN"]
NOTIFY_PAIR="USD-BTC"

def do_start(update: Update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Hello! Sent me something",
    )


def do_echo(update:Update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=update.message.text
    )


def do_chatid(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text= "Your ID is: {}".format(update.message.chat_id),
    )


def do_help(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="This is help page etc ... ",
    )


def do_time(update, context):
    proc = Popen(["date"], stdout=PIPE)
    text, error = proc.communicate()
    if error:
        text = "An error"
    else:
        text = text.decode("utf-8")

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )


def do_bitcoin(update, context):
    bttrx = BittrexClient()
    try:
        current_price = bttrx.get_last_price(pair=NOTIFY_PAIR)
        message = "{} = {}".format(NOTIFY_PAIR, current_price)
    except BittrexError:
        logger.error("BittrexError")
        message = "An error happend"

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=message
    )
    

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',
        level=logging.INFO,
    )
    updater = Updater(
        token=KEREELLXBOT_TOKEN,
        use_context=True,
    )

    bitcoin_handler = CommandHandler("bitcoin", do_bitcoin)
    help_handler = CommandHandler("help", do_help)
    time_handler = CommandHandler("time", do_time)
    start_handler = CommandHandler("start", do_start)
    get_id_handler = CommandHandler("chatid", do_chatid)
    echo_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(bitcoin_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(get_id_handler)
    updater.dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
