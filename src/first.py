#!/usr/bin/env python3
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
# from config import TELEGRAM_KEREELLXBOT_TOKEN
import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater = Updater(
    token=config.TELEGRAM_KEREELLXBOT_TOKEN,
    use_context=True
)

dispatcher = updater.dispatcher


def do_start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Talk to me",
    )


def do_menu(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Here will be menu",
    )


def do_echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text,
    )


def do_another(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Another method",
    )


def do_reply(update, context):
    update.message.reply_text("Now Replying")


cmd_start = CommandHandler('start', do_start)
dispatcher.add_handler(cmd_start)

cmd_start = CommandHandler("menu", do_menu)
dispatcher.add_handler(cmd_start)

event_echo = MessageHandler(Filters.text & (~Filters.command), do_echo)
dispatcher.add_handler(event_echo)

another_command = CommandHandler("another", do_another)
dispatcher.add_handler(another_command)

reply = CommandHandler("reply", do_reply)
dispatcher.add_handler(reply)

updater.start_polling()
