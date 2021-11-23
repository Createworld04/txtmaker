#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) xmysteriousx

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Hello There!",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command("help"))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Send Your Json File",
        reply_to_message_id=update.message_id
    )
