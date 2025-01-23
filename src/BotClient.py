# -*- coding: utf-8 -*-
import asyncio
import os
import random
import re
import datetime

from botpy.types.message import MarkdownPayload, KeyboardPayload

import messages.specificMessage
from random import randint
from botpy.manage import GroupManageEvent

from messages.specificMessage import HelloMessage
from .BotDB import BotDB
import botpy
from botpy import logging, BotAPI
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message
from .jiLLM import jiLLM

config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "secret", "config.yaml"))
test_config = read(config_path)

_log = logging.get_logger()


class MyClient(botpy.Client):
    #机器人主程序
    async def initial_bot(self,log_massage:str):
        await self.detect_special_time()
        self.llm = jiLLM()
        _log.info(log_massage)

    async def on_ready(self):
        await self.initial_bot(f"robot 「{self.robot.name}」 on_ready!")

    async def on_resumed(self):
        await self.initial_bot(f"robot 「{self.robot.name}」 on_resumed and time detection has started!")

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
        cmd = args[0]
        cmd_list = ["邦多利查卡","邦多利","旮旯给木","掷骰子","小锦一言"]
        cmd_target = [self.find_bangdream_card,self.random_Bangdream_pic,self.random_galgame_pic,self.roll_dice,self.famous_sentence]
        cmd_introduce = ["展示一张邦多利卡片","随机发送邦邦表情包","随机发送旮旯给木表情包","掷一个骰子(随机从1到6)","说一句名言"]
        for i in range(0,len(cmd_list)):
            if(cmd_list[i] == cmd):
                _log.info(f"{cmd}被找到")
                return cmd_target[i](args[1:])
        return "找不到指令，请输入.help获取帮助"

    def report_time(self,args):
        nowTime = "现在是 "
        youbi = datetime.datetime.now().weekday() + 1
        if(youbi == 1):
            nowTime += "星期一 "
        elif(youbi == 2):
            nowTime += "星期二 "
        elif(youbi == 3):
            nowTime += "星期三 "
        elif(youbi == 4):
            nowTime += "星期四 "
        elif(youbi == 5):
            nowTime += "星期五 "
        elif(youbi == 6):
            nowTime += "星期六 "
        elif(youbi == 7):
            nowTime += "星期日 "

        nowTime += datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return nowTime

    def random_Bangdream_pic(self,args):
        picNum = 6#可以在这里修改表情包数量
        random_Pic = random.randint(1,picNum)
        file_url = f"http://112.124.43.86/bangDream/{random_Pic}.jpg"
        return file_url

    def random_galgame_pic(self,args):
        picNum = 10#可以在这里修改表情包数量
        random_Pic = random.randint(1,picNum)
        file_url = f"http://112.124.43.86/gal/{random_Pic}.jpg"
        return file_url

    def roll_dice(self,args):
        return f"掷骰子的结果是:{str(random.randint(1,6))}"

    def famous_sentence(self,args):
        mydb = BotDB()
        return mydb.get_one_famousWords()

    def find_bangdream_card(self,args):
        if (not args) or len(args) == 0:
            picNum = 250  # 可以在这里修改表情包数量
            random_Pic = random.randint(1, picNum)
            file_url = f"http://112.124.43.86/bangdream_card/{random_Pic}.png"
        else:
            target = int(args[0])
            if(target > 0 and target <= 2640):
                file_url = f"http://112.124.43.86/bangdream_card/{target}.png"
            else:
                return "邦多利查卡功能介绍\n使用方法: /邦多利查卡 [卡面ID]\n示例: /邦多利查卡 1582\n请确保卡面ID是一个整数，并且这个数字应当大于0并小于2641，否则会返回本消息"
        return file_url

    async def detect_special_time(self):
        pass
        # while(True):
        #     now = datetime.datetime.now()
        #     if now.minute == 30:
        #         _log.info(now.strftime("%H:%M:%S"))
        #     if now.hour == 7 and now.minute == 0:
        #         await self.send_subjective_message("早上七点了，该起床了!")
        #     elif now.hour == 12 and now.minute == 0:
        #         await self.send_subjective_message("中午十二点了，该吃午饭了!")
        #     elif now.hour == 17 and now.minute == 34:
        #         await self.send_subjective_message("下午五点半了，该吃晚饭了!")
        #     elif now.hour == 23 and now.minute == 30:
        #         await self.send_subjective_message("晚上十一点半了，该睡觉了!")
        #     await asyncio.sleep(60)

    async def send_template_keyboard(self,api: BotAPI, groupMessage: GroupMessage):
        markdown = MarkdownPayload(content="# 123 \n 今天是个好天气")
        await api.post_group_message(groupMessage.group_openid,msg_type = 2,markdown=markdown)

    async def on_group_at_message_create(self, message: GroupMessage):
        _log.info(f"消息在{message.group_openid}")
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