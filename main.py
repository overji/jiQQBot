# -*- coding: utf-8 -*-
import asyncio
import os
import random
import re
import datetime
import messages.specificMessage
from random import randint
from botpy.manage import GroupManageEvent

from messages.specificMessage import HelloMessage
from src.BotDB import BotDB
import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message
from src.jiLLM import jiLLM
from src.BotClient import MyClient

if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_messages=True
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "secret", "config.yaml"))
    test_config = read(config_path)

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], secret=test_config["secret"])