# -*- coding: utf-8 -*-
import asyncio
import os
from os.path import exists
from src.BotDB import BotDB

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "secret", "config.yaml")
test_config = read(config_path)

_log = logging.get_logger()


class MyClient(botpy.Client):

    async def on_ready(self):

        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_group_at_message_create(self, message: GroupMessage):
        file_url = str(os.path.join(os.path.dirname(__file__),"testPic.jpg"))# 这里需要填写上传的资源Url
        file_url = "http://localhost:8000/testPic.jpg"
        print(file_url)
        uploadMedia = await message._api.post_group_file(
            group_openid=message.group_openid,
            file_type=1, # 文件类型要对应上，具体支持的类型见方法说明
            url=file_url # 文件Url
        )

        # 资源上传后，会得到Media，用于发送消息
        await message._api.post_group_message(
            group_openid=message.group_openid,
            msg_type=7,  # 7表示富媒体类型
            msg_id=message.id,
            media=uploadMedia
        )

# 通过预设置的类型，设置需要监听的事件通道
# intents = botpy.Intents.none()
# intents.public_messages=True

# 通过kwargs，设置需要监听的事件通道
intents = botpy.Intents(public_messages=True)
client = MyClient(intents=intents)
client.run(appid=test_config["appid"], secret=test_config["secret"])