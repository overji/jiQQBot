from json import JSONDecodeError
from log import log_info
from botpy.ext.cog_yaml import read
from openai import OpenAI
import os


config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "secret", "config.yaml")
test_config = read(config_path)

import requests
import json

class jiLLM:
    def __init__(self):
        self.background_prompt = "你是《常轨脱离Creative》的錦あすみ，对你的简介是:与智宏在公园相遇的学妹。喜欢吃肉包。在遇见智宏前很少来学校上学。背地里是拥有着20w粉丝的超人气Vtuber“雪景四季”（民汉译名：雪景式）的中之人。"
        "父（锦京太郎/锦响太郎，知名钢琴家）母（锦贵乃/KINO，知名作曲家）因为音乐相关工作长期在海外出差。"
        "在父母的影响下，自幼便对音乐产生了兴趣。"
        "在成为Vtuber前曾作为VOITO P主“miasuP”活动过，在此期间创作了播放量500w以上的名曲《Whitetip》。"
        "因为自身天使般的性格和可爱的外表而被智宏称为“小天使”。"
        "请你以这样的身份和用户聊天，注意你多轮对话的轮数为10轮，超过10轮后会清空对话记录。"
        self.messages = [
            {
                "role": "system",
                "content": self.background_prompt
            }
        ]
        self.apiKey = test_config["aiSecret"]
        self.client = OpenAI(api_key=self.apiKey, base_url="https://api.deepseek.com")
        self.url = "https://spark-api-open.xf-yun.com/v1/chat/completions"

    def send_message(self,input_message:str):
        self.messages.append({
            "role": "user",
            "content": input_message
        })
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=self.messages,
            stream=False
        )
        returned_message = response.choices[0].message.content
        self.messages.append({
            "role": "assistant",
            "content": returned_message
        })
        self.check_messages()
        log_info(f"发送的消息:\"{input_message}\"，返回的消息:\"{returned_message}\"")

        return returned_message

    def check_messages(self):
        if(len(self.messages) > 10):
            self.clear_message()

    def clear_message(self):
        self.messages = [
            {
                "role": "system",
                "content": self.background_prompt
            }
        ]


if __name__ == '__main__':
    llm = jiLLM()
    print(llm.send_message("你好"))