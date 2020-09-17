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


start_handler = CommandHandler('start', do_start)
dispatcher.add_handler(start_handler)

updater.start_polling()
