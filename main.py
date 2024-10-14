# -*- coding: utf-8 -*-
import asyncio
import os
import random
import re
import datetime

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()


class MyClient(botpy.Client):
    def judge_special_message(self,message:str):
        message = message.strip()
        _log.info(message)
        if(message[0] == '.'):
            return self.simple_command(message[1:])
        if re.search("^我(.*)你$",message):
            _log.info("收到了对方信号")
            return f"我也{message[1:len(message) - 1]}你"
        else:
            return "你好啊"

    def simple_command(self,cmd:str):
        cmd_list = ["time","bang","gal"]
        cmd_target = [self.report_time,self.random_Bangdream_pic,self.random_galgame_pic]
        cmd_introduce = ["输出当前时间","随机发送邦邦表情包","随机发送旮旯给木表情包"]
        if cmd == "help":
            ans = "提示信息如下\n"
            for i in range(0, len(cmd_list)):
                ans += f".{cmd_list[i]} : {cmd_introduce[i]}\n"
            ans = ans.strip()
            return ans
        for i in range(0,len(cmd_list)):
            if(cmd_list[i] == cmd):
                _log.info(f"{cmd}被找到")
                return cmd_target[i]()
        return "找不到指令，请输入.help获取帮助"

    def report_time(self):
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

    def random_Bangdream_pic(self):
        picNum = 6#可以在这里修改表情包数量
        random_Pic = random.randint(1,picNum)
        file_url = f"http://112.124.43.86/bangDream/{random_Pic}.jpg"
        return file_url

    def random_galgame_pic(self):
        picNum = 10#可以在这里修改表情包数量
        random_Pic = random.randint(1,picNum)
        file_url = f"http://112.124.43.86/gal/{random_Pic}.jpg"
        return file_url


    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_group_at_message_create(self, message: GroupMessage):
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
                media = uploadMedia
            )
        else:
            messageResult = await message._api.post_group_message(
                group_openid=message.group_openid,
                  msg_type=0,
                  msg_id=message.id,
                  content=myInfo)

if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], secret=test_config["secret"])