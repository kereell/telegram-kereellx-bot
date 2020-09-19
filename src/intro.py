#!/usr/bin/env python3
import telegram
from telegram.ext import Updater

from config import TELEGRAM_KEREELLXBOT_TOKEN

telegram_kereellx = telegram.Bot(
    token=TELEGRAM_KEREELLXBOT_TOKEN
)

print(telegram_kereellx.get_me())
