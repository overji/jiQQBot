# -*- coding: utf-8 -*-
import os
import re

from botpy.types.message import MarkdownPayload, KeyboardPayload, MessageMarkdownParams

from botpy.manage import GroupManageEvent
from messages.specificMessage import HelloMessage
from .BotDB import BotDB
import botpy
from botpy import logging, BotAPI
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message
from .jiLLM import jiLLM
from plugins.PLUGIN_LOADER import parse_command

config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "secret", "config.yaml"))
test_config = read(config_path)

_log = logging.get_logger()


class MyClient(botpy.Client):
    #机器人主程序
    async def initial_bot(self,log_massage:str):
        self.llm = jiLLM()
        _log.info(log_massage)

    async def on_ready(self):
        await self.initial_bot(f"robot 「{self.robot.name}」 on_ready!")

    async def on_resumed(self):
        await self.initial_bot(f"robot 「{self.robot.name}」 on_resumed and time detection has started!")

    async def handle_send_markdown_by_template(self, message:GroupMessage):
        params = [
            MessageMarkdownParams(key="date", values=["	2025/1/22，星期三，农历腊月廿三"]),
            MessageMarkdownParams(key="score", values=["95"]),
            MessageMarkdownParams(key="comment", values=["大吉"]),
            MessageMarkdownParams(key="sentence", values=["我们最值得自豪的不在于从不跌倒，而在于每次跌倒之后都爬起来。"]),
            MessageMarkdownParams(key="cardnum", values=["029038"])
        ]
        markdown = MarkdownPayload(custom_template_id="102439716_1737512805", params=params)
        # 通过api发送回复消息
        await message._api.post_group_message(group_openid=message.group_openid,msg_type=2,msg_id=message.id,markdown=markdown)

    def judge_special_message(self,message:str):
        message = message.strip()
        _log.info(message)
        if(message[0] == '/'):
            return self.simple_command(message[1:].split(' '))
        if(message == "你好"):
            return HelloMessage()
        if re.search("^我(.*)你$",message):
            _log.info("收到了对方信号")
            return f"我也{message[1:len(message) - 1]}你"
        else:
            return self.llm.send_message(message)

    def simple_command(self,args):
        parse_command(args)

    async def on_group_at_message_create(self, message: GroupMessage):
        _log.info(f"消息在{message.group_openid}")
        await self.handle_send_markdown_by_template(message)
        return
        myInfo = self.judge_special_message(message.content)
        if re.search("^http",myInfo):
            uploadMedia = await message._api.post_group_file(
                group_openid=message.group_openid,
                file_type=1,
                url = myInfo
            )
            await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type = 7,
                msg_id = message.id,
                media = uploadMedia,
                content=""
            )
        else:
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                  msg_type=0,
                  msg_id=message.id,
                  content=myInfo)

    async def on_group_add_robot(self,event:GroupManageEvent):
        _log.info("机器人被添加到群聊：" + str(event))
        db = BotDB()
        db.insert_group_if_not_exists(event.group_openid)
        uploadMedia = await self.api.post_group_file(
            group_openid=event.group_openid,
            file_type=1,
            url=f"http://112.124.43.86/bangDream/5.jpg"
        )
        await self.api.post_group_message(
            group_openid=event.group_openid,
            msg_type=7,
            event_id=event.event_id,
            media=uploadMedia,
            content="大家好我是小锦，来点大家想看的东西啊"
        )

    async def on_group_del_robot(self,event:GroupManageEvent):
        db = BotDB()
        db.delete_group_if_exists(event.group_openid)
        _log.info("机器人被移除群聊：" + str(event))

    async def send_subjective_message(self,messageContent:str):
        db = BotDB()
        groups = db.get_all_groups() #group_openid的列表
        _log.info("正在发送消息")
        for g in groups:
            uploadMedia = await self.api.post_group_file(
                group_openid=g[0],
                file_type=1,
                url=f"http://112.124.43.86/bangDream/5.jpg"
            )
            await self.api.post_group_message(
                group_openid=g[0],
                msg_type=7,
                media=uploadMedia,
                content=messageContent
            )