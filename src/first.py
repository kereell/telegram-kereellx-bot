#!/usr/bin/env python3
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from config import TELEGRAM_KEREELLXBOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater = Updater(
    token=TELEGRAM_KEREELLXBOT_TOKEN,
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


start_command = CommandHandler('start', do_start)
dispatcher.add_handler(start_command)

menu_command = CommandHandler("menu", do_menu)
dispatcher.add_handler(menu_command)
updater.start_polling()
